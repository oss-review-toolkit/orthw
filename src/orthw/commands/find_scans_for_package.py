# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: 2023 Helio Chissini de Castro
from __future__ import annotations

import click
from psycopg2 import sql
from rich import print
from rich.pretty import pprint

from orthw.commands import command_group
from orthw.utils.database import list_scan_results, query_scandb


class Command:
    """orthw command - find-scans-for-package"""

    _command_name: str = "find-scans-for-package"

    def process(self, package_id: str) -> None:
        list_scan_results(package_id=package_id)

        count_sql: str = sql.literal(
            f"SELECT COUNT(*) FROM scan_results WHERE identifier LIKE '{package_id}'",  # noqa: S608
        )
        count: list[tuple[str, str]] | None = query_scandb(sql=count_sql)

        if not count:
            print("[bright_yellow]No results were found with this package id.[/bright_yellow]")

        print(f"[bright_blue]Found the above $count scan results for query string {package_id}.[/bright_blue]")
        print("[bright_blue]Press enter to delete them.[/bright_blue]")
        input()

        delete_sql: str = f"DELETE FROM scan_results WHERE identifier LIKE {package_id}"  # nosec B608  # noqa: S608
        result = query_scandb(sql=delete_sql)

        if result:
            pprint(result)


@command_group.command()
@click.argument("package_id")
def find_scans_for_package(package_id: str) -> None:
    Command().process(package_id=package_id)
