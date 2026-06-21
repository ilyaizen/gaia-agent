"""Stub — Nous rate guard removed in Gaia fork.

Minimal stubs so lazy imports from upstream code don't crash.
"""

from __future__ import annotations

from typing import Any, Mapping, Optional


def record_nous_rate_limit(*args: Any, **kwargs: Any) -> None:
    pass


def nous_rate_limit_remaining() -> Optional[float]:
    return None


def clear_nous_rate_limit() -> None:
    pass


def format_remaining(seconds: float) -> str:
    return ""


def is_genuine_nous_rate_limit(*args: Any, **kwargs: Any) -> bool:
    return False
