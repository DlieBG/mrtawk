# -*- coding: utf-8 -*-
"""
mrtawk - Advanced Anomaly Detection in Internet Routing
Copyright (C) 2024 Benedikt Schwering

This software is distributed under the terms of the MIT license.
It can be found in the LICENSE file or at https://opensource.org/licenses/MIT.

Author Benedikt SCHWERING <mail@bschwer.ing>
"""
from src.services.query import query as query_service
from src.models.query import QueryRequest
from pathlib import Path
from rich import print
import click

def query(mrt_input_path: Path, request: QueryRequest):
    """ Query the MRT archive for a subset of MRTs.

        Author:
            Benedikt SCHWERING <mail@bschwer.ing>

        Params:
            mrt_input_path (Path): The path to the MRT input directory.
            request (QueryRequest): The query request.
    """
    print(
        f'[green]\[start][/] Query with\n',
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

    if result.rib_file and click.confirm(
        text='Print RIB file?',
        default=False,
    ):
        print(f'[yellow]\[RIB][/]')
        print(f'   [purple]{result.rib_file}[/]')

    if len(result.mrt_files) > 0 and click.confirm(
            text='Print MRT files?',
            default=False,
    ):
        print(f'[yellow]\[MRT][/]')
        for mrt_file in result.mrt_files:
            print(f'   [purple]{mrt_file}[/]')
