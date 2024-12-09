# -*- coding: utf-8 -*-
"""
mrtawk - Advanced Anomaly Detection in Internet Routing
Copyright (C) 2024 Benedikt Schwering

This software is distributed under the terms of the MIT license.
It can be found in the LICENSE file or at https://opensource.org/licenses/MIT.

Author Benedikt SCHWERING <mail@bschwer.ing>
"""
from src.services.query import query as query_service
from src.models.mrt_scenario import MRTScenario
from src.models.query import QueryRequest
from pathlib import Path
from rich import print
import click


def append(mrt_input_path: Path, scenario_output_path: Path, request: QueryRequest):
    """ Append MRT data to an existing scenario.

        Author:
            Benedikt SCHWERING <mail@bschwer.ing>

        Params:
            mrt_input_path (Path): The path to the MRT input directory.
            scenario_output_path (Path): The path to the scenario output directory.
    """
    # Check if the scenario file exists
    if not (scenario_output_path / 'scenario.yml').exists():
        print(f'[red]\[error][/] Scenario file does not exist')
        return

    scenario = MRTScenario.model_validate_json(
        json_data=(scenario_output_path / 'scenario.yml').read_text(),
    )

    print(
        f'[green]\[start][/] Append with\n',
        f'   start datetime [cyan]{request.start_datetime}[/]\n',
        f'   end datetime [cyan]{request.start_datetime}[/]\n',
        f'   vendors [blue]{request.vendor}[/]\n',
        f'   peer names [blue]{request.peer_name}[/]\n',
        f'   bgp types [blue]{request.bgp_type}[/]\n',
    )

    result = query_service(
        mrt_input_path=mrt_input_path,
        request=request,
    )

    print(
        f'[yellow]\[finish][/] Query results\n',
        f'   rib file [red]{not not result.rib_file}[/]\n',
        f'   mrt files [red]{len(result.mrt_files)}[/]\n',
    )

    if len(result.mrt_files) > 0 and click.confirm(
            text='Print MRT files?',
            default=False,
    ):
        print(f'[yellow]\[MRT][/]')
        for mrt_file in result.mrt_files:
            print(f'   [purple]{mrt_file}[/]')

    if len(result.mrt_files) > 0 and click.confirm(
            text='Copy and append MRT files?',
            default=True,
    ):
        for mrt_file in result.mrt_files:
            (scenario_output_path / mrt_file.name).write_bytes(
                data=mrt_file.read_bytes(),
            )
            scenario.mrt_files.append(mrt_file.name)

        # Remove duplicates and sort mrt files
        scenario.mrt_files = list(set(scenario.mrt_files))
        scenario.mrt_files.sort()

        (scenario_output_path / 'scenario.yml').write_text(
            data=scenario.model_dump_json(
                indent=4,
            ),
        )

        print(f'[yellow]\[info][/] Scenario file updated')
