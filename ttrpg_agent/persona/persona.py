"""
Author: Joon Sung Park (joonspk@stanford.edu)

File: persona.py
Description: Defines the Persona class that powers the agents in Reverie.

Note (May 1, 2023) -- this is effectively GenerativeAgent class. Persona was
the term we used internally back in 2022, taking from our Social Simulacra
paper.
"""

import math
import sys
import datetime
import random

sys.path.append("../")

from global_methods import *

from persona.memory_structures.spatial_memory import *
from persona.memory_structures.associative_memory import *
from persona.memory_structures.scratch import *

from persona.cognitive_modules.perceive import *
from persona.cognitive_modules.retrieve import *
from persona.cognitive_modules.plan import *
from persona.cognitive_modules.reflect import *
from persona.cognitive_modules.execute import *
from persona.cognitive_modules.converse import *


class Persona:
    def __init__(self, name, folder_mem_saved=False):
        # PERSONA BASE STATE
        # <name> is the full name of the persona. This is a unique identifier for
        # the persona within Reverie.
        self.name = name

        # PERSONA MEMORY
        # If there is already memory in folder_mem_saved, we load that. Otherwise,
        # we create new memory instances.
        # <s_mem> is the persona's spatial memory.
        f_s_mem_saved = f"{folder_mem_saved}/bootstrap_memory/spatial_memory.json"
        self.s_mem = MemoryTree(f_s_mem_saved)
        # <a_mem> is the persona's associative memory.
        f_a_mem_saved = f"{folder_mem_saved}/bootstrap_memory/associative_memory"
        self.a_mem = AssociativeMemory(f_a_mem_saved)
        # <scratch> is the persona's scratch (short term memory) space.
        scratch_saved = f"{folder_mem_saved}/bootstrap_memory/scratch.json"
        self.scratch = Scratch(scratch_saved)

    def save(self, save_folder):
        """
        Save persona's current state (i.e., memory).

        INPUT:
          save_folder: The folder where we wil be saving our persona's state.
        OUTPUT:
          None
        """
        # Spatial memory contains a tree in a json format.
        # e.g., {"double studio":
        #         {"double studio":
        #           {"bedroom 2":
        #             ["painting", "easel", "closet", "bed"]}}}
        f_s_mem = f"{save_folder}/spatial_memory.json"
        self.s_mem.save(f_s_mem)

        # Associative memory contains a csv with the following rows:
        # [event.type, event.created, event.expiration, s, p, o]
        # e.g., event,2022-10-23 00:00:00,,Isabella Rodriguez,is,idle
        f_a_mem = f"{save_folder}/associative_memory"
        self.a_mem.save(f_a_mem)

        # Scratch contains non-permanent data associated with the persona. When
        # it is saved, it takes a json form. When we load it, we move the values
        # to Python variables.
        f_scratch = f"{save_folder}/scratch.json"
        self.scratch.save(f_scratch)

# TTRPG Player Agent will not have vision in this same way and anything to do with the maze will have to be reworked. Perception will be based on the current scene. I do not know if att_bandwidth will be relevant. However, retention will be important to keep the agent focused on the most relevant task at hand.
    def perceive(self, event):
        """
        This function takes a narrative event (text input) and returns it as a perceived event.
        In the TTRPG context, perception is simply recording what was told to the agent.

        INPUT:
          event: A narrative event (e.g., a tuple or string representing what the agent perceives)
        OUTPUT:
          a list containing the perceived event(s)
        """
        return [event]

    def retrieve(self, perceived):
        """
        This function takes the events that are perceived by the persona as input
        and returns a set of related events and thoughts that the persona would
        need to consider as context when planning.

        INPUT:
          perceive: a list of <ConceptNode> that are perceived and new.
        OUTPUT:
          retrieved: dictionary of dictionary. The first layer specifies an event,
                     while the latter layer specifies the "curr_event", "events",
                     and "thoughts" that are relevant.
        """
        return retrieve(self, perceived)

    def plan(self, maze, personas, new_day, retrieved):
        """
        Main cognitive function of the chain. In the TTRPG context, planning is based on narrative memory and context only.

        INPUT:
          maze: (Unused, kept for compatibility; pass None)
          personas: (Unused, kept for compatibility; pass None)
          new_day: Indicates if it's a new narrative phase or day
          retrieved: dictionary of dictionary. The first layer specifies an event,
                     while the latter layer specifies the "curr_event", "events",
                     and "thoughts" that are relevant.
        OUTPUT
          The target action address of the persona (persona.scratch.act_address).
        """
        return plan(self, None, None, new_day, retrieved)

    def execute(self, maze, personas, plan):
        """
        This function takes the agent's current plan and outputs a narrative response.

        INPUT:
          maze: (Unused, kept for compatibility; pass None)
          personas: (Unused, kept for compatibility; pass None)
          plan: The target action address of the persona (persona.scratch.act_address).
        OUTPUT:
          execution: A triple set that contains the following components:
            <next_tile>: (Unused, kept for compatibility)
            <pronunciatio>: (Unused, kept for compatibility)
            <description>: A string description of the agent's narrative response.
        """
        return execute(self, None, None, plan)

    def reflect(self):
        """
        Reviews the persona's memory and create new thoughts based on it.

        INPUT:
          None
        OUTPUT:
          None
        """
        reflect(self)

    def move(self, maze, personas, curr_tile, curr_time):
        """
        This is the main cognitive function where our main sequence is called.

        INPUT:
          maze: The Maze class of the current world.
          personas: A dictionary that contains all persona names as keys, and the
                    Persona instance as values.
          curr_tile: A tuple that designates the persona's current tile location
                     in (row, col) form. e.g., (58, 39)
          curr_time: datetime instance that indicates the game's current time.
        OUTPUT:
          execution: A triple set that contains the following components:
            <next_tile> is a x,y coordinate. e.g., (58, 9)
            <pronunciatio> is an emoji.
            <description> is a string description of the movement. e.g.,
            writing her next novel (editing her novel)
            @ double studio:double studio:common room:sofa
        """
        # Updating persona's scratch memory with <curr_tile>.
        self.scratch.curr_tile = curr_tile

        # We figure out whether the persona started a new day, and if it is a new
        # day, whether it is the very first day of the simulation. This is
        # important because we set up the persona's long term plan at the start of
        # a new day.
        new_day = False
        if not self.scratch.curr_time:
            new_day = "First day"
        elif self.scratch.curr_time.strftime("%A %B %d") != curr_time.strftime(
            "%A %B %d"
        ):
            new_day = "New day"
        self.scratch.curr_time = curr_time

        # Main cognitive sequence begins here.
        perceived = self.perceive(maze)
        retrieved = self.retrieve(perceived)
        plan = self.plan(maze, personas, new_day, retrieved)
        self.reflect()

        # <execution> is a triple set that contains the following components:
        # <next_tile> is a x,y coordinate. e.g., (58, 9)
        # <pronunciatio> is an emoji. e.g., "\ud83d\udca4"
        # <description> is a string description of the movement. e.g.,
        #   writing her next novel (editing her novel)
        #   @ double studio:double studio:common room:sofa
        return self.execute(maze, personas, plan)

    def open_convo_session(self, convo_mode):
        open_convo_session(self, convo_mode)
