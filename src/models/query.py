# -*- coding: utf-8 -*-
"""
mrtawk - Advanced Anomaly Detection in Internet Routing
Copyright (C) 2024 Benedikt Schwering

This software is distributed under the terms of the MIT license.
It can be found in the LICENSE file or at https://opensource.org/licenses/MIT.

Author Benedikt SCHWERING <mail@bschwer.ing>
"""
from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from pathlib import Path

VENDOR_CHOICES = ['lw']
PEER_NAME_CHOICES = [
    'amsix', 'decix', 'franceix', 'linx', 'marseix', 'mskix', 'nlix', 'swissix',
    'chinatel', 'cogent', 'dtag', 'gtt', 'hurricane', 'level3', 'ntt', 'pccw', 'rostel', 'seabone', 'swisscom', 'telia',
]
BGP_TYPE_CHOICES = ['rib', 'update']

class QueryRequest(BaseModel):
    """ Query request model.

        Author:
            Benedikt SCHWERING <mail@bschwer.ing>
    """
    start_datetime: datetime
    end_datetime: datetime
    vendor: list[str] # lw, ...
    peer_name: list[str] # amsix, decix, chinatel, ...
    bgp_type: list[str] # rib, update, ...

class QueryResponse(BaseModel):
    """ Query response model.

        Author:
            Benedikt SCHWERING <mail@bschwer.ing>
    """
    mrt_files: list[Path]
    rib_file: Optional[Path]
