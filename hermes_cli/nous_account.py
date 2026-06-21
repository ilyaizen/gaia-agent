"""Stub — Nous account/portal removed in Gaia fork.

Minimal stubs so lazy imports from upstream code don't crash.
In production, Nous provider is not configured and these paths are never hit.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Optional


NousAccountInfoSource = str  # placeholder type

TOOL_COVERAGE_CATEGORIES: tuple[str, ...] = ()


@dataclass(frozen=True)
class NousPortalSubscriptionInfo:
    plan: Optional[str] = None
    tier: Optional[int] = None
    monthly_charge: Optional[float] = None
    monthly_credits: Optional[float] = None
    current_period_end: Optional[str] = None
    credits_remaining: Optional[float] = None
    rollover_credits: Optional[float] = None


@dataclass(frozen=True)
class NousPaidServiceAccessInfo:
    allowed: Optional[bool] = None
    paid_access: Optional[bool] = None
    reason: Optional[str] = None
    organisation_id: Optional[str] = None
    effective_at_ms: Optional[int] = None
    has_active_subscription: Optional[bool] = None
    active_subscription_is_paid: Optional[bool] = None
    subscription_tier: Optional[int] = None
    subscription_monthly_charge: Optional[float] = None
    subscription_credits_remaining: Optional[float] = None
    purchased_credits_remaining: Optional[float] = None
    total_usable_credits: Optional[float] = None
    browser_use_entitled: bool = False
    computer_use_entitled: bool = False


@dataclass(frozen=True)
class NousPortalAccountInfo:
    source: Any = "none"
    user_id: Optional[str] = None
    email: Optional[str] = None
    org_id: Optional[str] = None
    subscription: Optional[NousPortalSubscriptionInfo] = None
    paid_service: Optional[NousPaidServiceAccessInfo] = None
    tool_access: dict = field(default_factory=dict)

    @property
    def is_logged_in(self) -> bool:
        return False

    @property
    def has_active_paid_subscription(self) -> bool:
        return False


def get_nous_portal_account_info(**kwargs: Any) -> NousPortalAccountInfo:
    """Stub: always returns logged-out account."""
    return NousPortalAccountInfo()


def nous_portal_topup_url(*args: Any, **kwargs: Any) -> str:
    return ""


def format_nous_portal_entitlement_message(*args: Any, **kwargs: Any) -> str:
    return ""
