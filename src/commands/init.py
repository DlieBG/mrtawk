# -*- coding: utf-8 -*-
"""
mrtawk - Advanced Anomaly Detection in Internet Routing
Copyright (C) 2024 Benedikt Schwering

This software is distributed under the terms of the MIT license.
It can be found in the LICENSE file or at https://opensource.org/licenses/MIT.

Author Benedikt SCHWERING <mail@bschwer.ing>
"""
from src.models.mrt_scenario import MRTScenario
from pathlib import Path
from rich import print
from uuid import uuid4
import click

def init(scenario_output_path: Path):
    """ Initialize a new scenario and write it to a file.

        Author:
            Benedikt SCHWERING <mail@bschwer.ing>

        Params:
            scenario_output_path (Path): The path to the scenario output directory.
    """
    # Check if the scenario file already exists and ask for overwrite
    if (scenario_output_path / 'scenario.json').exists():
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

    (scenario_output_path / 'scenario.json').write_text(
        data=scenario.model_dump_json(
            indent=4,
        ),
    )

    print(f'[yellow]\[info][/] Scenario file created')
