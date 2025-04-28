"""
Mock implementations of dependencies for the TTRPG Generative Agent.

This module provides mock implementations of the dependencies that the Persona
class relies on, such as the Maze class, other personas, and time handling.
These mocks allow us to run the Persona class outside of the original simulation
environment.
"""

import datetime
import json
import os
from typing import Dict, List, Set, Tuple, Any, Optional


class MockMaze:
    """
    Mock implementation of the Maze class from the original codebase.
    
    The original Maze class represents a 2D grid environment that agents navigate.
    This mock provides the same interface but returns simplified data.
    """
    
    def __init__(self, maze_name="mock_maze"):
        """
        Initialize a mock maze.
        
        Args:
            maze_name: Name of the maze (not used in the mock, but kept for compatibility)
        """
        self.maze_name = maze_name
        self.tiles = {}  # Dictionary to store tile data
        
        # Create a simple default tile that can be returned
        self.default_tile = {
            "world": "ttrpg_world",
            "sector": "current_scene",
            "arena": "narrative_space",
            "game_object": "",
            "events": set(),
        }
    
    def access_tile(self, coords: Tuple[int, int]) -> Dict:
        """
        Access a tile at the given coordinates.
        
        Args:
            coords: A tuple of (x, y) coordinates
            
        Returns:
            A dictionary representing the tile data
        """
        # If the tile exists, return it; otherwise, return the default tile
        if coords in self.tiles:
            return self.tiles[coords]
        return self.default_tile.copy()
    
    def get_nearby_tiles(self, coords: Tuple[int, int], radius: int) -> List[Tuple[int, int]]:
        """
        Get a list of tile coordinates within the given radius of the given coordinates.
        
        Args:
            coords: A tuple of (x, y) coordinates
            radius: The radius to search within
            
        Returns:
            A list of tile coordinates
        """
        # In the mock, we'll just return the given coordinates
        return [coords]
    
    def add_event_from_tile(self, event: Tuple, coords: Tuple[int, int]) -> None:
        """
        Add an event to a tile.
        
        Args:
            event: A tuple representing an event
            coords: A tuple of (x, y) coordinates
        """
        # Create the tile if it doesn't exist
        if coords not in self.tiles:
            self.tiles[coords] = self.default_tile.copy()
            self.tiles[coords]["events"] = set()
        
        # Add the event to the tile
        self.tiles[coords]["events"].add(event)
    
    def remove_event_from_tile(self, event: Tuple, coords: Tuple[int, int]) -> None:
        """
        Remove an event from a tile.
        
        Args:
            event: A tuple representing an event
            coords: A tuple of (x, y) coordinates
        """
        # If the tile exists and the event is in the tile, remove it
        if coords in self.tiles and event in self.tiles[coords]["events"]:
            self.tiles[coords]["events"].remove(event)
    
    def remove_subject_events_from_tile(self, subject: str, coords: Tuple[int, int]) -> None:
        """
        Remove all events with the given subject from a tile.
        
        Args:
            subject: The subject of the events to remove
            coords: A tuple of (x, y) coordinates
        """
        # If the tile exists, remove all events with the given subject
        if coords in self.tiles:
            events_to_remove = []
            for event in self.tiles[coords]["events"]:
                if event[0] == subject:
                    events_to_remove.append(event)
            
            for event in events_to_remove:
                self.tiles[coords]["events"].remove(event)
    
    def turn_event_from_tile_idle(self, event: Tuple, coords: Tuple[int, int]) -> None:
        """
        Turn an event from a tile idle.
        
        Args:
            event: A tuple representing an event
            coords: A tuple of (x, y) coordinates
        """
        # In the mock, we'll just remove the event
        self.remove_event_from_tile(event, coords)


class MockTime:
    """
    Mock implementation of time handling for the TTRPG Generative Agent.
    
    This class provides a simple way to manage time in the TTRPG context,
    replacing the datetime handling in the original codebase.
    """
    
    def __init__(self, start_time=None):
        """
        Initialize the mock time.
        
        Args:
            start_time: The starting time (defaults to current time)
        """
        self.current_time = start_time or datetime.datetime.now()
        self.turn_counter = 0
    
    def advance_time(self, seconds=0, minutes=0, hours=0, days=0):
        """
        Advance the time by the given amount.
        
        Args:
            seconds: Number of seconds to advance
            minutes: Number of minutes to advance
            hours: Number of hours to advance
            days: Number of days to advance
        """
        self.current_time += datetime.timedelta(
            seconds=seconds,
            minutes=minutes,
            hours=hours,
            days=days
        )
        self.turn_counter += 1
    
    def get_current_time(self):
        """
        Get the current time.
        
        Returns:
            The current datetime
        """
        return self.current_time
    
    def get_turn_counter(self):
        """
        Get the current turn counter.
        
        Returns:
            The current turn counter
        """
        return self.turn_counter


class MockPersonas:
    """
    Mock implementation of the personas dictionary from the original codebase.
    
    This class provides a dictionary-like object that simulates other agents.
    """
    
    def __init__(self):
        """
        Initialize the mock personas.
        """
        self.personas = {}
    
    def add_persona(self, name, persona):
        """
        Add a persona to the dictionary.
        
        Args:
            name: The name of the persona
            persona: The persona object
        """
        self.personas[name] = persona
    
    def get_persona(self, name):
        """
        Get a persona from the dictionary.
        
        Args:
            name: The name of the persona
            
        Returns:
            The persona object, or None if not found
        """
        return self.personas.get(name)
    
    def __getitem__(self, key):
        """
        Get a persona from the dictionary using dictionary syntax.
        
        Args:
            key: The name of the persona
            
        Returns:
            The persona object
            
        Raises:
            KeyError: If the persona is not found
        """
        if key not in self.personas:
            raise KeyError(f"Persona '{key}' not found")
        return self.personas[key]
    
    def __setitem__(self, key, value):
        """
        Set a persona in the dictionary using dictionary syntax.
        
        Args:
            key: The name of the persona
            value: The persona object
        """
        self.personas[key] = value
    
    def __contains__(self, key):
        """
        Check if a persona is in the dictionary using 'in' syntax.
        
        Args:
            key: The name of the persona
            
        Returns:
            True if the persona is in the dictionary, False otherwise
        """
        return key in self.personas
    
    def keys(self):
        """
        Get the keys of the dictionary.
        
        Returns:
            The keys of the dictionary
        """
        return self.personas.keys()
    
    def values(self):
        """
        Get the values of the dictionary.
        
        Returns:
            The values of the dictionary
        """
        return self.personas.values()
    
    def items(self):
        """
        Get the items of the dictionary.
        
        Returns:
            The items of the dictionary
        """
        return self.personas.items()


def create_text_event(text, subject=None, predicate=None, object=None):
    """
    Create an event tuple from text input.
    
    This function converts text input into an event tuple that can be used
    by the Persona class. In the original codebase, events are represented
    as tuples of (subject, predicate, object, description).
    
    Args:
        text: The text input
        subject: The subject of the event (defaults to "narrative")
        predicate: The predicate of the event (defaults to "describes")
        object: The object of the event (defaults to "scene")
        
    Returns:
        A tuple representing the event
    """
    subject = subject or "narrative"
    predicate = predicate or "describes"
    object = object or "scene"
    
    return (subject, predicate, object, text)
