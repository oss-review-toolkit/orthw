# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: 2023 Helio Chissini de Castro
from __future__ import annotations

from orthw import config
from orthw.commands import command_group
from orthw.utils.process import run


class Command:
    """orthw command - handled-licenses"""

    _command_name: str = "handled-licenses"

    def process(self) -> None:
        """_summary_"""

        args: list[str] = [
            "orth",
            "list-license-categories",
            "--license-classifications-file",
            config.get("ort_config_license_classifications_file"),
        ]

        run(args)


@command_group.command(
    context_settings={"orthw_group": "NO_SCAN_CONTEXT"},
)
def handled_licenses() -> None:
    Command().process()
