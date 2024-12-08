# -*- coding: utf-8 -*-
"""
mrtawk - Advanced Anomaly Detection in Internet Routing
Copyright (C) 2024 Benedikt Schwering

This software is distributed under the terms of the MIT license.
It can be found in the LICENSE file or at https://opensource.org/licenses/MIT.

Author Benedikt SCHWERING <mail@bschwer.ing>
"""
from pydantic import BaseModel
from typing import Optional

class MRTScenario(BaseModel):
    '''
    This class represents an MRT scenario.

    Author:
        Benedikt Schwering <mail@bschwer.ing>
    '''
    name: str
    description: str
    no_rabbitmq_direct: bool
    rabbitmq_grouped: Optional[int]
    no_mongodb_log: bool
    no_mongodb_state: bool
    no_mongodb_statistics: bool
    clear_mongodb: bool
    playback_speed: Optional[int]
    mrt_files: list[str]
