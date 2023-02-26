# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: 2023 Helio Chissini de Castro

import click
from psycopg2 import sql
from rich import print

from orthw.commandbase import CommandBase, command_group
from orthw.utils.database import list_scan_results, query_scandb


# ----------------------------------
# Command Line options and arguments


class OrtHWCommand(CommandBase):
    """orthw command - delete-scan-results"""

    _command_name: str = "delete-scan-results"

    def process(self, package_id: str) -> None:
        # Prevent SQL injection assigning as literal
        safe_pid = sql.Literal(package_id)

        list_scan_results(config=self.config, package_id=package_id)

        count_sql: str = f"SELECT COUNT(*) FROM scan_results WHERE identifier LIKE '{safe_pid}'"  # nosec B608
        count: list[tuple[str, str]] | None = query_scandb(config=self.config, sql=count_sql)

        if not count:
            print("[bright_yellow]No results were found with this package id.[/bright_yellow]")

        print(f"[bright_blue]Found the above $count scan results for query string {package_id}.[/bright_blue]")
        print("[bright_blue]Press enter to delete them.[/bright_blue]")
        input()

        delete_sql: str = f"DELETE FROM scan_results WHERE identifier LIKE {safe_pid}"  # nosec B608
        query_scandb(config=self.config, sql=delete_sql)


@command_group.command()
@click.argument("package_id")
def delete_scan_results(package_id: str) -> None:
    OrtHWCommand().process(package_id)
