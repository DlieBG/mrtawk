# -*- coding: utf-8 -*-
"""
mrtawk - Advanced Anomaly Detection in Internet Routing
Copyright (C) 2024 Benedikt Schwering

This software is distributed under the terms of the MIT license.
It can be found in the LICENSE file or at https://opensource.org/licenses/MIT.

Author Benedikt SCHWERING <mail@bschwer.ing>
"""
from src.commands.init import init as init_command
from pathlib import Path
from rich import print
import click

@click.group(
    chain=True,
)
@click.option(
    '--mrt-input-path',
    '-i',
    type=click.Path(
        dir_okay=True,
        file_okay=False,
        resolve_path=True,
        exists=True,
    ),
    default='.',
)
@click.option(
    '--scenario-output-path',
    '-o',
    type=click.Path(
        dir_okay=True,
        file_okay=False,
        resolve_path=True,
    ),
    required=True,
)
@click.pass_context
def cli(ctx: click.Context, mrt_input_path: str, scenario_output_path: str):
    """ Initialize the CLI context with the input and output paths.

        Author:
            Benedikt SCHWERING <mail@bschwer.ing>

        Params:
            ctx (click.Context): The Click context.
            mrt_input_path (str): The path to the MRT input directory.
            scenario_output_path (str): The path to the scenario output directory.
    """
    ctx.ensure_object(dict)
    ctx.obj['mrt_input_path'] = mrt_input_path
    ctx.obj['scenario_output_path'] = scenario_output_path

    mrt_input_path = Path(mrt_input_path)
    scenario_output_path = Path(scenario_output_path)

    print(
        f'[green]\[start][/] mrtawk with\n',
        f'   mrt input [purple]{mrt_input_path}[/]\n',
        f'   scenario output [purple]{scenario_output_path}[/]',
    )

    # Create the scenario output directory if it does not exist
    if not scenario_output_path.exists():
        scenario_output_path.mkdir(
            parents=True,
            exist_ok=True,
        )
        print(f'[yellow]\[info][/] Scenario directory created')

@cli.command(
    'init',
)
@click.pass_obj
def init(obj: dict):
    """ Initialize a new scenario and write it to a file.

        Author:
            Benedikt SCHWERING <bes9584@thi.de>

        Params:
            obj (dict): The dictionary containing the CLI arguments.
    """
    init_command(
        obj=obj,
    )

@cli.command(
    'append',
)
@click.pass_obj
def append(obj: dict):
    """ Append MRT data to an existing scenario.

        Author:
            Benedikt SCHWERING <mail@bschwer.ing>

        Params:
            obj (dict): The dictionary containing the CLI arguments.
    """
    mrt_input_path = Path(obj['mrt_input_path'])
    scenario_output_path = Path(obj['scenario_output_path'])

    # Check if the scenario file exists
    if not (scenario_output_path / 'scenario.yml').exists():
        print(f'[red]\[error][/] Scenario file does not exist')
        return

    # Todo: Implement append command
