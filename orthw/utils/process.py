# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: 2023 Helio Chissini de Castro

import subprocess  # nosec
from typing import Any

from orthw.utils.logging import log, console
from orthw.utils.required import required_command


def run(args: list[str], live_output: bool = False) -> int | Any:
    """Run a process with defined arguments

    :param args: Arguments
    :type args: list[str]
    :param live_output: If you want to have log output, defaults to False
    :type live_output: bool, optional
    :return: Process resulting code
    :rtype: int | Any
    """
    # Expect first argument be the required command
    main_cmd = required_command(args[0])
    if not main_cmd:
        return None

    # Replace main command with path qualified one
    args[0] = main_cmd

    log.debug(f"command line: [bright_green]{' '.join(args)}[/]", extra={"markup": True})

    proc = subprocess.Popen(args, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)  # nosec
    if live_output:
        if proc.stdout:
            while True:
                output = proc.stdout.readline()
                if proc.poll() is not None:
                    break
                if output:
                    console.print(output.decode("utf-8").strip(), style="bright_white")

    res = proc.wait()
    log.debug(f"Return code: {res}")
    return res
