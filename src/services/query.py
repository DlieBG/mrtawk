# -*- coding: utf-8 -*-
"""
mrtawk - Advanced Anomaly Detection in Internet Routing
Copyright (C) 2024 Benedikt Schwering

This software is distributed under the terms of the MIT license.
It can be found in the LICENSE file or at https://opensource.org/licenses/MIT.

Author Benedikt SCHWERING <mail@bschwer.ing>
"""
from src.models.query import QueryRequest, QueryResponse
from datetime import datetime
from pathlib import Path
from rich import print

def query(mrt_input_path: Path, request: QueryRequest) -> QueryResponse:
    """ Query the MRT archive for a subset of MRTs.

        Author:
            Benedikt SCHWERING <mail@bschwer.ing>

        Params:
            mrt_input_path (Path): The path to the MRT input directory.
            request (QueryRequest): The query request.

        Returns:
            QueryResponse: The query response.
    """
    response = QueryResponse(
        mrt_files=[],
        rib_file=None,
    )

    for path in mrt_input_path.glob('**/*.bz2'):
        try:
            # Extract the timestamp from the MRT file name
            # Only consider MRT files within the selected time range
            timestamp = datetime.strptime(
                '_'.join(path.name.split('_')[0:2]),
                '%Y%m%d_%H%M'
            )
            if not request.start_datetime <= timestamp < request.end_datetime:
                continue

            # Extract the vendor from the MRT file name
            # Only consider MRT files from the selected vendor
            vendor = path.name.split('_')[4]
            if vendor not in request.vendor:
                continue

            # Extract the peer name from the MRT file name
            # Only consider MRT files from the selected peer
            peer_name = path.name.split('_')[6]
            if peer_name not in request.peer_name:
                continue

            # Extract the BGP type from the MRT file name
            # Only consider MRT files of the selected BGP type
            bgp_type = path.name.split('_')[7].split('.')[0]
            if bgp_type not in request.bgp_type:
                continue

            if bgp_type == 'rib':
                response.rib_file = path
            if bgp_type == 'update':
                response.mrt_files.append(path)
        except:
            print(f'[red]\[warning][/] Cannot parse MRT file [purple]{path}[/]')

    response.mrt_files.sort()

    return response
