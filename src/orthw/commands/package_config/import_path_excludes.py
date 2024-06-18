# Copyright 2023 The ORTHW Project Authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# SPDX-License-Identifier: Apache-2.0
# License-Filename: LICENSE
from __future__ import annotations

import click

from pathlib import Path

from orthw import config
from orthw.utils import logging
from orthw.utils.cmdgroups import package_config_group
from orthw.utils.process import run
from orthw.utils.required import require_initialized


def import_path_excludes(package_id: str, source_code_dir: str) -> None:
    require_initialized()

    package_configuration_file: Path = "FIXME find_package(package_id)"
    exports_path_excludes_file: Path = config.exports_path_excludes_file
    source_code_dir: Path = config.source_code_dir
    exports_vcs_url_mapping_file: Path = config.exports_vcs_url_mapping_file

    args: list[str] = [
        "orth",
        "package-configuration",
        "import-path-excludes",
        "--package-configuration-file".
        package_configuration_file,
        "--path-excludes-file",
        exports_path_excludes_file.as_posix(),
        "--source-code-dir",
        source_code_dir.as_posix()
    ]

    run(args=args)


@package_config_group.command(
    context="PACKAGE_CONFIG",
    name="import-path-excludes",
    help="""
        Import path excludes from a file into package configuration file for given package id.

        Examples:

        orthw package-config import-path-excludes Maven:org.apache.curator:curator-framework:2.13.0 /home/ort-user/code-repo/
    """,
    short_help="Import path excludes from a file into package configuration file for given package id."
)
@click.argument("package_id")
@click.argument("source_code_dir")
def __import_path_excludes(package_id: str) -> None:
    """Import path excludes from a file into package configuration file for given package id."""
    import_path_excludes(package_id=package_id, source_code_dir=source_code_dir)
