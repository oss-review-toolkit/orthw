# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: 2023 Helio Chissini de Castro

import sys
from tempfile import TemporaryDirectory

import click

from orthw import config
from orthw.commandbase import CommandBase, command_group
from orthw.utils import logging
from orthw.utils.process import run
from orthw.utils.checksum import check_evaluation_md5_sum


class Command(CommandBase):
    """orthw command - analyze"""

    _command_name: str = "analyze"

    def evaluate(self, format: str = "JSON") -> None:
        """Use Ort analyzer command on provided source dir

        :param source_code_dir: Source directory to be evaluated
        :type source_code_dir: str
        """

        if not check_evaluation_md5_sum():
            # Skip evaluation as the input files haven't changed.
            return

        temp_dir = TemporaryDirectory()

        args: list[str] = [
            "ort",
            "evaluate",
            "--copyright-garbage-file",
            config.get("ort_config_copyright_garbage_file"),
            "--package-curations-dir",
            config.get("ort_config_package_curations_dir"),
            "--output-dir",
            temp_dir.name,
            "--output-formats",
            "JSON",
            "--ort-file",
            config.get("scan_result_file"),
            "--repository-configuration-file",
            config.get("repository_configuration_file"),
            "--rules-file",
            config.get("ort_config_rules_file"),
            "--license-classifications-file",
            config.get("ort_config_license_classifications_file"),
            "--package-configuration-dir",
            config.get("ort_config_package_configuration_dir"),
        ]

        # Execute external run
        if run(args=args):
            logging.error("Error running the evaluator.")
            sys.exit(1)


@command_group.command()
@click.option("--format", "-f", default="JSON")
def evaluate(format: str) -> None:
    Command().evaluate()
