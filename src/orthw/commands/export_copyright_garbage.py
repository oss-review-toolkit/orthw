# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: 2023 Helio Chissini de Castro
from __future__ import annotations

import tempfile
from pathlib import Path

from rich.pretty import pprint

from orthw import config
from orthw.commands import command_group
from orthw.utils import logging
from orthw.utils.process import run
from orthw.utils.required import require_initialized


class Command:
    """orthw command - export-copyright-garbage"""

    _command_name: str = "export-copyright-garbage"

    def export_copyright_garbage(self) -> None:
        """Command export-copyright-garbage"""
        require_initialized()

        copyrights_file: str = config.get("copyrights_file")
        ort_config_copyright_garbage_file = config.get("ort_config_copyright_garbage_file")
        scan_result_file = config.get("scan_result_file")
        if copyrights_file is None or ort_config_copyright_garbage_file is None or scan_result_file is None:
            logging.error("Configuration invalid.")
            return

        logging.info(f"Exporting from {copyrights_file} to {ort_config_copyright_garbage_file}.")

        tmpdir = tempfile.TemporaryDirectory(prefix="orthw_")
        mapped_copyrights_file: Path = Path(tmpdir.name / "copyrights-mapped.txt")  # type: ignore

        args: list[str] = [
            "orth",
            "map-copyrights",
            "--input-copyrights-file",
            copyrights_file,
            "--output-copyrights-file",
            mapped_copyrights_file.as_posix(),
            "--ort-file",
            scan_result_file,
        ]
        run(args=args)

        logging.info("Mapped the given processed statements to the following unprocessed ones:")
        if mapped_copyrights_file.exists():
            with Path.open(mapped_copyrights_file) as f:
                pprint(f.readlines())

        args = [
            "orth",
            "import-copyright-garbage",
            "--input-copyright-garbage-file",
            mapped_copyrights_file.as_posix(),
            "--output-copyright-garbage-file",
            ort_config_copyright_garbage_file,
        ]
        run(args=args)


@command_group.command()
def export_copyright_garbage() -> None:
    Command().export_copyright_garbage()