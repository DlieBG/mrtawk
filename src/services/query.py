# -*- coding: utf-8 -*-
"""
mrtawk - Advanced Anomaly Detection in Internet Routing
Copyright (C) 2024 Benedikt Schwering

This software is distributed under the terms of the MIT license.
It can be found in the LICENSE file or at https://opensource.org/licenses/MIT.

Author Benedikt SCHWERING <mail@bschwer.ing>
"""
from src.models.query import QueryRequest, QueryResponse
from pathlib import Path

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
    # Todo: Implement query service
    pass
