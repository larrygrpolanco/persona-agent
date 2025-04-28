# TTRPG Generative Agent

This project adapts the Generative Agents architecture from the paper "Generative Agents: Interactive Simulacra of Human Behavior" for use in tabletop role-playing games (TTRPGs), specifically the game ECH0.

## Overview

The original Generative Agents architecture was designed for a 2D simulation environment where agents navigated a virtual town, followed daily schedules, and interacted with each other. This project adapts that architecture for a text-based TTRPG context, where agents play roles (Pilot or Child) in the ECH0 game.

## Project Structure

- `persona/`: The core agent code, copied from the original codebase
- `mocks.py`: Mock implementations of dependencies (Maze, other personas, time handling)
- `test_harness.py`: A simple test harness for instantiating and testing the agent

## Getting Started

### Prerequisites

- Python 3.7+
- Access to a language model API (e.g., OpenAI's GPT-3.5-turbo)

### Installation

1. Clone the repository
2. Install the required dependencies (TBD)

### Running the Test Harness

To run the test harness with the Pilot role:

```bash
python ttrpg_agent/test_harness.py --role pilot
```

To run the test harness with the Child role:

```bash
python ttrpg_agent/test_harness.py --role child
```

## Usage

Once the test harness is running, you can enter text input to process through the agent's cognitive cycle. The agent will respond with its generated output.

Special commands:
- `quit`: Exit the test harness
- `memory`: View the agent's memory (events, thoughts, chats)

Example session:

```
Initialized Pilot Persona
Enter text input to process through the Persona's cognitive cycle
Enter 'quit' to exit
Enter 'memory' to view the Persona's memory

> The children lead you to a rusted mech slumped against a cliff.

Pilot: I feel a sense of recognition as I see the rusted mech. This could be a clue to finding my final resting place. I'll ask the children more about this mech and how they found it.

> memory

Associative Memory (Events):
Pilot is a ghost (2025-04-28 10:56:42)
Pilot has a mission (2025-04-28 10:56:42)
Pilot was on a last mission (2025-04-28 10:56:42)
Pilot left behind loved ones (2025-04-28 10:56:42)
narrative describes scene (2025-04-28 10:56:42): The children lead you to a rusted mech slumped against a cliff.

Associative Memory (Thoughts):
This mech might be related to my past (2025-04-28 10:56:42)
I should ask the children more about this mech (2025-04-28 10:56:42)

Associative Memory (Chats):
```

## Development Status

This project is in the early stages of development. The current focus is on creating a standalone test harness that can instantiate a Persona and run its cognitive cycle with text input.

## Next Steps

1. Test the basic cognitive cycle with simple text input
2. Adapt the perception system for text-based input
3. Modify the planning system for narrative contributions
4. Enhance the reflection system for character development
5. Improve memory retrieval for narrative relevance
