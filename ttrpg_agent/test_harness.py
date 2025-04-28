"""
Test harness for the TTRPG Generative Agent.

This module provides a simple test harness for the TTRPG Generative Agent,
allowing us to instantiate a Persona and test its cognitive cycle with text input.
"""

import os
import sys
import json
import datetime
import argparse
from typing import Dict, List, Tuple, Any, Optional

# Add the parent directory to the path so we can import the persona module
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import the Persona class and mocks
from ttrpg_agent.persona.persona import Persona
from ttrpg_agent.mocks import MockMaze, MockTime, MockPersonas, create_text_event


def create_bootstrap_memory_folder(role: str) -> str:
    """
    Create a bootstrap memory folder for the Persona.
    
    Args:
        role: The role of the Persona (Pilot or Child)
        
    Returns:
        The path to the bootstrap memory folder
    """
    # Create a folder for the bootstrap memory
    folder_path = f"ttrpg_agent/bootstrap_memory_{role.lower()}"
    os.makedirs(folder_path, exist_ok=True)
    os.makedirs(f"{folder_path}/bootstrap_memory", exist_ok=True)
    
    return folder_path


def initialize_spatial_memory(folder_path: str) -> None:
    """
    Initialize the spatial memory for the Persona.
    
    Args:
        folder_path: The path to the bootstrap memory folder
    """
    # Create a simple spatial memory structure
    spatial_memory = {
        "ttrpg_world": {
            "current_scene": {
                "narrative_space": []
            }
        }
    }
    
    # Write the spatial memory to a file
    with open(f"{folder_path}/bootstrap_memory/spatial_memory.json", "w") as f:
        json.dump(spatial_memory, f, indent=2)


def initialize_associative_memory(folder_path: str, role: str) -> None:
    """
    Initialize the associative memory for the Persona.
    
    Args:
        folder_path: The path to the bootstrap memory folder
        role: The role of the Persona (Pilot or Child)
    """
    # Create the associative memory directory
    os.makedirs(f"{folder_path}/bootstrap_memory/associative_memory", exist_ok=True)
    
    # Create empty files for the associative memory
    with open(f"{folder_path}/bootstrap_memory/associative_memory/events.csv", "w") as f:
        f.write("type,created,expiration,subject,predicate,object,description\n")
    
    with open(f"{folder_path}/bootstrap_memory/associative_memory/thoughts.csv", "w") as f:
        f.write("type,created,expiration,subject,predicate,object,description\n")
    
    with open(f"{folder_path}/bootstrap_memory/associative_memory/chat.csv", "w") as f:
        f.write("type,created,expiration,subject,predicate,object,description\n")
    
    # Add initial memories based on the role
    with open(f"{folder_path}/bootstrap_memory/associative_memory/events.csv", "a") as f:
        if role.lower() == "pilot":
            # Add Pilot-specific memories
            f.write(f'event,{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")},,Pilot,is,a ghost,The Pilot is a ghost of a dead mech Pilot, backed up in a tiny ECHO drive just before death.\n')
            f.write(f'event,{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")},,Pilot,has,a mission,The Pilot\'s mission is to find where they fell.\n')
            f.write(f'event,{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")},,Pilot,was on,a last mission,The Pilot was on their last mission when they died.\n')
            f.write(f'event,{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")},,Pilot,left behind,loved ones,The Pilot left behind loved ones when they died.\n')
        elif role.lower() == "child":
            # Add Child-specific memories
            f.write(f'event,{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")},,Child,found,an ECHO drive,The Child found an ECHO drive while playing among the wreckage of giant mechs of war.\n')
            f.write(f'event,{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")},,Child,lives in,a peaceful land,The Child lives in a land at peace, where scars of a great war have healed over the decades.\n')
            f.write(f'event,{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")},,Child,plays among,mech wreckage,The Child plays among the wreckage of giant mechs of war.\n')
            f.write(f'event,{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")},,Child,met,a Pilot ghost,The Child met a ghost of a dead mech Pilot, backed up in a tiny ECHO drive.\n')


def initialize_scratch(folder_path: str, role: str) -> None:
    """
    Initialize the scratch memory for the Persona.
    
    Args:
        folder_path: The path to the bootstrap memory folder
        role: The role of the Persona (Pilot or Child)
    """
    # Create a simple scratch memory structure
    scratch = {
        "curr_time": datetime.datetime.now().strftime("%B %d, %Y, %H:%M:%S"),
        "curr_tile": (0, 0),
        "name": role,
        "first_name": role,
        "last_name": "",
        "age": 30 if role.lower() == "pilot" else 10,
        "innate": "determined, stoic, nostalgic" if role.lower() == "pilot" else "curious, adventurous, empathetic",
        "learned": "",
        "currently": f"seeking final resting place" if role.lower() == "pilot" else f"helping the Pilot find their final resting place",
        "lifestyle": "",
        "living_area": "ECHO drive" if role.lower() == "pilot" else "village",
        "occupation": "former mech Pilot" if role.lower() == "pilot" else "child",
        "daily_plan": [],
        "curr_day_schedule": [],
        "planned_path": [],
        "chat": "",
        "chatting_with": "",
        "chatting_with_buffer": {},
        "act_address": "",
        "act_obj_str": "",
        "act_description": "",
        "act_pronunciatio": "",
        "act_event": "",
        "act_obj_event": "",
        "act_start_time": "",
        "act_duration": 0,
        "act_status": "",
        "act_obj_status": "",
        "act_block_reason": "",
        "conversation_with": "",
        "conversation_contexts": [],
        "conversation_history": [],
        "conversation_state": "",
        "conversation_memory": [],
        "conversation_summary": "",
        "conversation_last_time": "",
        "conversation_end_time": "",
        "conversation_topic": "",
        "conversation_tone": "",
        "conversation_goal": "",
        "conversation_strategy": "",
        "conversation_response": "",
        "conversation_response_time": "",
        "conversation_response_duration": 0,
        "conversation_response_status": "",
        "conversation_response_block_reason": "",
        "conversation_response_event": "",
        "conversation_response_obj_event": "",
        "conversation_response_obj_status": "",
        "conversation_response_obj_str": "",
        "conversation_response_address": "",
        "conversation_response_description": "",
        "conversation_response_pronunciatio": "",
        "conversation_response_start_time": "",
        "conversation_response_duration": 0,
        "conversation_response_status": "",
        "conversation_response_obj_status": "",
        "conversation_response_block_reason": "",
    }
    
    # Write the scratch memory to a file
    with open(f"{folder_path}/bootstrap_memory/scratch.json", "w") as f:
        json.dump(scratch, f, indent=2)


def initialize_persona(role: str) -> Tuple[Persona, MockMaze, MockTime, MockPersonas]:
    """
    Initialize a Persona with the given role.
    
    Args:
        role: The role of the Persona (Pilot or Child)
        
    Returns:
        A tuple of (Persona, MockMaze, MockTime, MockPersonas)
    """
    # Create the bootstrap memory folder
    folder_path = create_bootstrap_memory_folder(role)
    
    # Initialize the memory structures
    initialize_spatial_memory(folder_path)
    initialize_associative_memory(folder_path, role)
    initialize_scratch(folder_path, role)
    
    # Create the mock objects
    mock_maze = MockMaze()
    mock_time = MockTime()
    mock_personas = MockPersonas()
    
    # Create the Persona
    persona = Persona(role, folder_path)
    
    return persona, mock_maze, mock_time, mock_personas


def process_text_input(persona: Persona, mock_maze: MockMaze, mock_personas: MockPersonas, 
                      mock_time: MockTime, text: str) -> str:
    """
    Process text input through the Persona's cognitive cycle.
    
    Args:
        persona: The Persona to process the input
        mock_maze: The MockMaze object
        mock_personas: The MockPersonas object
        mock_time: The MockTime object
        text: The text input
        
    Returns:
        The Persona's response
    """
    # Create an event from the text
    event = create_text_event(text)
    
    # Add the event to the mock maze
    mock_maze.add_event_from_tile(event, persona.scratch.curr_tile)
    
    # Update the Persona's current time
    persona.scratch.curr_time = mock_time.get_current_time()
    
    # Run the Persona's cognitive cycle
    perceived = persona.perceive(mock_maze)
    retrieved = persona.retrieve(perceived)
    plan = persona.plan(mock_maze, mock_personas, False, retrieved)
    persona.reflect()
    next_tile, pronunciatio, description = persona.execute(mock_maze, mock_personas, plan)
    
    # Advance the mock time
    mock_time.advance_time(minutes=5)
    
    # Return the Persona's response
    return description


def main():
    """
    Main function for the test harness.
    """
    # Parse command line arguments
    parser = argparse.ArgumentParser(description="Test harness for the TTRPG Generative Agent")
    parser.add_argument("--role", type=str, choices=["pilot", "child"], default="pilot",
                        help="The role of the Persona (Pilot or Child)")
    args = parser.parse_args()
    
    # Initialize the Persona
    persona, mock_maze, mock_time, mock_personas = initialize_persona(args.role)
    
    print(f"Initialized {args.role.capitalize()} Persona")
    print("Enter text input to process through the Persona's cognitive cycle")
    print("Enter 'quit' to exit")
    print("Enter 'memory' to view the Persona's memory")
    print()
    
    # Main loop
    while True:
        # Get input from the user
        text = input("> ")
        
        # Check for special commands
        if text.lower() == "quit":
            break
        elif text.lower() == "memory":
            print("\nAssociative Memory (Events):")
            print(persona.a_mem.get_str_seq_events())
            print("\nAssociative Memory (Thoughts):")
            print(persona.a_mem.get_str_seq_thoughts())
            print("\nAssociative Memory (Chats):")
            print(persona.a_mem.get_str_seq_chats())
            continue
        
        # Process the input
        response = process_text_input(persona, mock_maze, mock_personas, mock_time, text)
        
        # Print the response
        print(f"\n{persona.name}: {response}\n")


if __name__ == "__main__":
    main()
