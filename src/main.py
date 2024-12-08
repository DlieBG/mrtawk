# -*- coding: utf-8 -*-
"""
mrtawk - Advanced Anomaly Detection in Internet Routing
Copyright (C) 2024 Benedikt Schwering

This software is distributed under the terms of the MIT license.
It can be found in the LICENSE file or at https://opensource.org/licenses/MIT.

Author Benedikt SCHWERING <mail@bschwer.ing>
"""
from src.models.query import QueryRequest, VENDOR_CHOICES, PEER_NAME_CHOICES, BGP_TYPE_CHOICES
from src.commands.append import append as append_command
from src.commands.query import query as query_command
from src.commands.init import init as init_command
from datetime import datetime
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
        scenario_output_path=Path(obj['scenario_output_path']),
    )

@cli.command(
    'append',
)
@click.pass_obj
@click.option(
    '--start-datetime',
    '-s',
    type=datetime,
    required=True,
)
@click.option(
    '--end-datetime',
    '-e',
    type=datetime,
    required=True,
)
@click.option(
    '--vendor',
    '-v',
    type=click.Choice(
        choices=VENDOR_CHOICES,
    ),
    multiple=True,
    required=True,
    default=['lw'],
    show_default=True,
)
@click.option(
    '--peer-name',
    '-p',
    type=click.Choice(
        choices=PEER_NAME_CHOICES,
    ),
    multiple=True,
    required=True,
    default=['decix'],
    show_default=True,
)
@click.option(
    '--bgp-type',
    '-b',
    type=click.Choice(
        choices=BGP_TYPE_CHOICES,
    ),
    multiple=True,
    required=True,
    default=['update'],
    show_default=True,
)
def append(obj: dict, start_datetime: datetime, end_datetime: datetime, vendor: list[str], peer_name: list[str], bgp_type: list[str]):
    """ Append MRT data to an existing scenario.

        Author:
            Benedikt SCHWERING <mail@bschwer.ing>

        Params:
            obj (dict): The dictionary containing the CLI arguments.
            start_datetime (datetime): The start datetime.
            end_datetime (datetime): The end datetime.
            vendor (list[str]): The vendor(s).
            peer_name (list[str]): The peer name(s).
            bgp_type (list[str]): The BGP type(s).
    """
    append_command(
        mrt_input_path=Path(obj['mrt_input_path']),
        scenario_output_path=Path(obj['scenario_output_path']),
        request=QueryRequest(
            start_datetime=start_datetime,
            end_datetime=end_datetime,
            vendor=vendor,
            peer_name=peer_name,
            bgp_type=bgp_type,
        ),
    )

@cli.command(
    'query',
)
@click.pass_obj
@click.option(
    '--start-datetime',
    '-s',
    type=datetime,
    required=True,
)
@click.option(
    '--end-datetime',
    '-e',
    type=datetime,
    required=True,
)
@click.option(
    '--vendor',
    '-v',
    type=click.Choice(
        choices=VENDOR_CHOICES,
    ),
    multiple=True,
    required=True,
    default=['lw'],
    show_default=True,
)
@click.option(
    '--peer-name',
    '-p',
    type=click.Choice(
        choices=PEER_NAME_CHOICES,
    ),
    multiple=True,
    required=True,
    default=['decix'],
    show_default=True,
)
@click.option(
    '--bgp-type',
    '-b',
    type=click.Choice(
        choices=BGP_TYPE_CHOICES,
    ),
    multiple=True,
    required=True,
    default=['update'],
    show_default=True,
)
def query(obj: dict, start_datetime: datetime, end_datetime: datetime, vendor: list[str], peer_name: list[str], bgp_type: list[str]):
    """ Query the MRT archive for a subset of MRTs.

        Author:
            Benedikt SCHWERING <mail@bschwer.ing>

        Params:
            obj (dict): The dictionary containing the CLI arguments.
            start_datetime (datetime): The start datetime.
            end_datetime (datetime): The end datetime.
            vendor (list[str]): The vendor(s).
            peer_name (list[str]): The peer name(s).
            bgp_type (list[str]): The BGP type(s).
    """
    query_command(
        mrt_input_path=Path(obj['mrt_input_path']),
        request=QueryRequest(
            start_datetime=start_datetime,
            end_datetime=end_datetime,
            vendor=vendor,
            peer_name=peer_name,
            bgp_type=bgp_type,
        ),
    )
