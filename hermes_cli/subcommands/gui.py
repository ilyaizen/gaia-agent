"""``gaia desktop`` / ``gaia gui`` subcommand — stubbed out.

The Electron desktop app is stripped from the Gaia fork.
This stub prints a helpful message and exits cleanly.
"""

from __future__ import annotations

import sys
from typing import Callable


def build_gui_parser(subparsers, *, cmd_gui: Callable) -> None:  # noqa: ARG001
    """Attach a no-op ``desktop``/``gui`` subcommand."""
    gui_parser = subparsers.add_parser(
        "desktop",
        aliases=["gui"],
        help="Not available in Gaia fork (Electron GUI stripped)",
        description=(
            "The Electron desktop app is not part of the Gaia fork. "
            "Use the CLI or messaging gateway instead."
        ),
    )
    gui_parser.set_defaults(func=cmd_gui)
