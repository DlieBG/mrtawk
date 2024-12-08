# -*- coding: utf-8 -*-
"""
mrtawk - Advanced Anomaly Detection in Internet Routing
Copyright (C) 2024 Benedikt Schwering

This software is distributed under the terms of the MIT license.
It can be found in the LICENSE file or at https://opensource.org/licenses/MIT.

Author Benedikt SCHWERING <mail@bschwer.ing>
"""
from src.models.query import QueryRequest
from pathlib import Path

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

    # Todo: Implement append command
