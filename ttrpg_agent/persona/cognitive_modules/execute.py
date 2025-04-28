"""
Author: Joon Sung Park (joonspk@stanford.edu)

File: execute.py
Description: This defines the "Act" module for generative agents.
"""

import sys
import random

sys.path.append("../../")

from global_methods import *
from path_finder import *
from utils import *


def execute(persona, maze, personas, plan):
    """
    In the TTRPG context, this function takes the agent's current plan and outputs a narrative response.

    INPUT:
      persona: Current <Persona> instance.
      maze: (Unused, kept for compatibility; pass None)
      personas: (Unused, kept for compatibility; pass None)
      plan: The target action address of the persona (persona.scratch.act_address).

    OUTPUT:
      execution: A triple set that contains the following components:
        <next_tile>: (Unused, kept for compatibility)
        <pronunciatio>: (Unused, kept for compatibility)
        <description>: A string description of the agent's narrative response.
    """
    # In the TTRPG context, we simply return the current action description as the narrative response.
    description = f"{persona.scratch.act_description}"
    return (None, None, description)
