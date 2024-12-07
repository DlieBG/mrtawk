# -*- coding: utf-8 -*-
"""
mrtawk - Advanced Anomaly Detection in Internet Routing
Copyright (C) 2024 Benedikt Schwering

This software is distributed under the terms of the MIT license.
It can be found in the LICENSE file or at https://opensource.org/licenses/MIT.

Author Benedikt SCHWERING <bes9584@thi.de>
"""
from src.models.mrt_scenario import MRTScenario
from pathlib import Path
from rich import print
from uuid import uuid4
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
def cli(ctx, mrt_input_path: str, scenario_output_path: str):
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
    scenario_output_path = Path(obj['scenario_output_path'])

    if (scenario_output_path / 'scenario.yml').exists():
        print(f'[red]\[warning][/] Scenario file already exists')
        click.confirm(
            text='Do you want to overwrite it?',
            abort=True,
        )

    print(f'[green]\[start][/] Initialize scenario')

    scenario = MRTScenario(
        name=click.prompt(
            text='Name',
            default=f'Scenario {str(uuid4())}',
        ),
        description=click.prompt(
            text='Description',
            default='',
        ),
        no_rabbitmq_direct=not click.confirm(
            text='RabbitMQ direct',
            default=True,
        ),
        rabbitmq_grouped=click.prompt(
            text='RabbitMQ Grouped Interval',
            default=5,
            type=int,
        ) if click.confirm(
            text='RabbitMQ Grouped',
            default=False,
        ) else None,
        no_mongodb_log=not click.confirm(
            text='MongoDB Log',
            default=False,
        ),
        no_mongodb_state=not click.confirm(
            text='MongoDB State',
            default=False,
        ),
        no_mongodb_statistics=not click.confirm(
            text='MongoDB Statistics',
            default=False,
        ),
        clear_mongodb=click.confirm(
            text='Clear MongoDB',
            default=True,
        ),
        playback_speed=click.prompt(
            text='Playback Speed Value',
            default=1,
            type=int,
        ) if click.confirm(
            text='Playback Speed',
            default=False,
        ) else None,
        mrt_files=[],
    )

    (scenario_output_path / 'scenario.yml').write_text(
        data=scenario.model_dump_json(
            indent=4,
        ),
    )

    print(f'[yellow]\[info][/] Scenario file created')

@cli.command(
    'append',
)
@click.pass_obj
def append(obj: dict):
    mrt_input_path = Path(obj['mrt_input_path'])
    scenario_output_path = Path(obj['scenario_output_path'])

    if not (scenario_output_path / 'scenario.yml').exists():
        print(f'[red]\[error][/] Scenario file does not exist')
        return

    # Todo: Implement append command
