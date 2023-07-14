# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: 2023 Helio Chissini de Castro
from __future__ import annotations

from rich import print

from orthw.commands import command_group

# ----------------------------------
# Command Line options and arguments


class OrtHWCommand:
    """orthw command - rc-generate-rule-violation-resolutions"""

    _command_name: str = "rc-generate-rule-violation-resolutions"

    def process(self) -> None:
        print("\n[sandy_brown]This command is not implemented yet.[/sandy_brown]")


@command_group.command(
    context_settings={"orthw_group": "REPOSITORY_CONFIG"},
)
def rc_generate_rule_violation_resolutions() -> None:
    OrtHWCommand().process()
