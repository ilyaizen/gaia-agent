"""Stub — Nous billing removed in Gaia fork.

Minimal stubs so lazy imports from upstream code don't crash.
"""

from __future__ import annotations

from typing import Any, Optional


class BillingError(Exception):
    pass


class BillingScopeRequired(BillingError):
    pass


class BillingRateLimited(BillingError):
    pass


class BillingAuthError(BillingError):
    pass


def resolve_portal_base_url(state: Optional[dict[str, Any]] = None) -> str:
    return ""


def get_billing_state(*, timeout: float = 10) -> dict[str, Any]:
    return {}


def patch_auto_top_up(*args: Any, **kwargs: Any) -> dict[str, Any]:
    raise BillingError("Nous billing not available in Gaia fork")


def post_charge(*args: Any, **kwargs: Any) -> dict[str, Any]:
    raise BillingError("Nous billing not available in Gaia fork")


def get_charge_status(*args: Any, **kwargs: Any) -> dict[str, Any]:
    raise BillingError("Nous billing not available in Gaia fork")
