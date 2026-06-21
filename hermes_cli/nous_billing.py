"""Stub — Nous billing removed in Gaia fork.

Minimal stubs so lazy imports from upstream code don't crash.
In production, Nous provider is not configured and these paths are never hit.
"""

from __future__ import annotations

import os
import urllib.parse
from typing import Any, Optional

DEFAULT_PORTAL_BASE_URL = "https://portal.nousresearch.com"


class BillingError(Exception):
    """A billing HTTP call failed (stub for Gaia fork)."""

    def __init__(
        self,
        message: str = "",
        *,
        status: Optional[int] = None,
        error: Optional[str] = None,
        portal_url: Optional[str] = None,
        retry_after: Optional[int] = None,
        payload: Optional[dict[str, Any]] = None,
    ) -> None:
        super().__init__(message)
        self.status = status
        self.error = error
        self.portal_url = portal_url
        self.retry_after = retry_after
        self.payload = payload or {}


class BillingScopeRequired(BillingError):
    pass


class BillingRateLimited(BillingError):
    pass


class BillingAuthError(BillingError):
    pass


def resolve_portal_base_url(state: Optional[dict[str, Any]] = None) -> str:
    """Resolve the portal base URL with login-time precedence."""
    env = os.getenv("HERMES_PORTAL_BASE_URL") or os.getenv("NOUS_PORTAL_BASE_URL")
    if env and env.strip():
        return env.strip().rstrip("/")
    if state:
        stored = state.get("portal_base_url")
        if isinstance(stored, str) and stored.strip():
            return stored.strip().rstrip("/")
    return DEFAULT_PORTAL_BASE_URL


def get_billing_state(*, timeout: float = 10) -> dict[str, Any]:
    return {}


def patch_auto_top_up(*args: Any, **kwargs: Any) -> dict[str, Any]:
    raise BillingError("Nous billing not available in Gaia fork", error="nous_unavailable")


def post_charge(*args: Any, **kwargs: Any) -> dict[str, Any]:
    raise BillingError("Nous billing not available in Gaia fork", error="idempotency_key_required")


def get_charge_status(*args: Any, **kwargs: Any) -> dict[str, Any]:
    raise BillingError("Nous billing not available in Gaia fork", error="invalid_charge_id")


def _absolutize_portal_url(portal_url: Optional[str]) -> Optional[str]:
    """Resolve a (possibly relative) server portalUrl to an absolute URL."""
    if not (isinstance(portal_url, str) and portal_url.strip()):
        return portal_url
    base = resolve_portal_base_url()
    return urllib.parse.urljoin(base.rstrip("/") + "/", portal_url)


def _retry_after_seconds(headers: Any) -> Optional[int]:
    """Parse a Retry-After header (integer seconds) — None if absent/bad."""
    if headers is None:
        return None
    try:
        raw = headers.get("Retry-After")
    except Exception:
        raw = None
    if raw is None:
        return None
    try:
        return int(str(raw).strip())
    except (TypeError, ValueError):
        return None


def _raise_for_error(
    status: int, payload: dict[str, Any], headers: Any = None
) -> None:
    """Map an HTTP error response to the right typed BillingError."""
    error = payload.get("error") if isinstance(payload, dict) else None
    message = payload.get("message") if isinstance(payload, dict) else None
    portal_url = _absolutize_portal_url(
        payload.get("portalUrl") if isinstance(payload, dict) else None
    )
    retry_after = _retry_after_seconds(headers)

    common = {
        "status": status,
        "error": error,
        "portal_url": portal_url,
        "retry_after": retry_after,
        "payload": payload if isinstance(payload, dict) else None,
    }

    if status == 401:
        raise BillingAuthError(message or "Authentication required.", **common)
    if status == 403 and error == "insufficient_scope":
        raise BillingScopeRequired(
            message or "This action needs the billing:manage scope.", **common
        )
    if status in (429, 503):
        raise BillingRateLimited(
            message or "Rate limited — try again shortly.", **common
        )
    raise BillingError(message or error or f"Billing request failed ({status}).", **common)
