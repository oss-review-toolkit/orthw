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

from pathlib import Path

import click

from orthw import config
from orthw.utils import logging
from orthw.utils.cmdgroups import repository_group
from orthw.utils.process import run
from orthw.utils.required import require_initialized

def sort_() -> None:
    require_initialized()

    repository_configuration_file: Path = config.repository_configuration_file.as_posix()

    args: list[str] = [
        "orth",
        "repository-configuration",
        "sort",
        repository_configuration_file
    ]

    run(args=args)


@repository_group.command(
    name="sort",
    help="Alphabetically sorts the excludes and curation entries in the ort.yml file within orthw initialized directory.",
    options_metavar="REPOSITORY_CONFIG",
    short_help="Alphabetically sorts entries in the ort.yml file within orthw initialized directory."
)
def __sort() -> None:
    sort_()
