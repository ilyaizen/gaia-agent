"""Stub — Nous subscription removed in Gaia fork.

Minimal stubs so lazy imports from upstream code don't crash.
In production, Nous provider is not configured and these paths are never hit.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, Iterable, Optional, Set

from hermes_cli.nous_account import NousPortalAccountInfo


@dataclass(frozen=True)
class NousFeatureState:
    key: str
    label: str
    included_by_default: bool = False
    available: bool = False
    active: bool = False
    managed_by_nous: bool = False
    direct_override: bool = False
    toolset_enabled: bool = False
    current_provider: str = ""
    explicit_configured: bool = False


@dataclass
class NousSubscriptionFeatures:
    subscribed: bool = False
    nous_auth_present: bool = False
    provider_is_nous: bool = False
    features: Dict[str, NousFeatureState] = field(default_factory=dict)
    account_info: Optional[NousPortalAccountInfo] = None

    @property
    def web(self) -> NousFeatureState:
        return self.features.get("web", NousFeatureState(key="web", label="Web"))

    @property
    def image_gen(self) -> NousFeatureState:
        return self.features.get("image_gen", NousFeatureState(key="image_gen", label="Image Gen"))

    @property
    def tts(self) -> NousFeatureState:
        return self.features.get("tts", NousFeatureState(key="tts", label="TTS"))

    @property
    def stt(self) -> NousFeatureState:
        return self.features.get("stt", NousFeatureState(key="stt", label="STT"))

    @property
    def browser(self) -> NousFeatureState:
        return self.features.get("browser", NousFeatureState(key="browser", label="Browser"))

    @property
    def video_gen(self) -> NousFeatureState:
        return self.features.get("video_gen", NousFeatureState(key="video_gen", label="Video Gen"))


def get_nous_subscription_features(
    config: Optional[Dict[str, object]] = None,
    *,
    force_fresh: bool = False,
) -> NousSubscriptionFeatures:
    """Stub: always returns unsubscribed (all tools available)."""
    return NousSubscriptionFeatures()


def apply_nous_managed_defaults(config: Dict[str, Any]) -> Dict[str, Any]:
    """Stub: no-op, returns config unchanged."""
    return config


def prompt_enable_tool_gateway(*args: Any, **kwargs: Any) -> Any:
    """Stub: no-op."""
    return None
