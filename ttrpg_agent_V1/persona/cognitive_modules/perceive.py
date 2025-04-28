"""
Author: Joon Sung Park (joonspk@stanford.edu)

File: perceive.py
Description: This defines the "Perceive" module for generative agents.
"""

import sys

sys.path.append("../../")

from operator import itemgetter
from global_methods import *
from persona.prompt_template.gpt_structure import *
from persona.prompt_template.run_gpt_prompt import *


def generate_poig_score(persona, event_type, description):
    if "is idle" in description:
        return 1

    if event_type == "event":
        return run_gpt_prompt_event_poignancy(persona, description)[0]
    elif event_type == "chat":
        return run_gpt_prompt_chat_poignancy(persona, persona.scratch.act_description)[
            0
        ]


def perceive(persona, event):
    """
    Perceives a narrative event (text input) and returns it as a perceived event.
    In the TTRPG context, perception is simply recording what was told to the agent.

    INPUT:
      persona: An instance of <Persona> that represents the current persona.
      event: A narrative event (e.g., a tuple or string representing what the agent perceives)
    OUTPUT:
      ret_events: a list containing the perceived event(s)
    """
    return [event]
