# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: 2023 Helio Chissini de Castro
from __future__ import annotations

import ctypes
import logging as stdlogger
import os

from rich.console import Console
from rich.logging import RichHandler

# Setup the main logger message
stdlogger.basicConfig(level="INFO", format="%(message)s", datefmt="[%X]", handlers=[RichHandler(markup=True)])
# Global log variable
logging = stdlogger.getLogger("rich")

# Global console output
console = Console()


def admin() -> bool:
    # We not allow run as a root/admin
    try:
        is_admin = os.getuid() == 0
    except AttributeError:  # We're playing Windows game
        is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0  # type: ignore

    return is_admin
