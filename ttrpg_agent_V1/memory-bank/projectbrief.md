# Project Brief: TTRPG Generative Agent

## Overview
Create a generative agent capable of playing a role in the TTRPG game ECH0, adapting the architecture from the "Generative Agents: Interactive Simulacra of Human Behavior" research paper. The agent will be able to play either the Pilot or Child role, engaging in storytelling, world-building, and dialogue while maintaining memory and planning capabilities.

## Core Objectives

1. **Extract and Adapt Core Agent Architecture**: Isolate the Persona system from the original codebase, removing dependencies on the 2D simulation environment (maze, schedules, etc.) while preserving the memory, planning, and reflection capabilities.

2. **Text-Based Perception**: Replace the spatial perception system with a text-based perception system that can understand TTRPG game state, narrative elements, and player interactions.

3. **Role-Playing Capabilities**: Enable the agent to understand and play within the rules and narrative structure of ECH0, taking on either the Pilot or Child role with appropriate behaviors, knowledge, and emotional responses.

4. **Memory and Narrative Coherence**: Maintain the agent's ability to remember past events, form reflections, and create a coherent narrative experience across a complete game session.

## Success Criteria

1. A standalone agent that can be initialized with a character role (Pilot/Child)
2. The agent can process text input describing game state and player actions
3. The agent can generate appropriate in-character responses, maintaining consistency with its role and past interactions
4. The agent demonstrates memory of previous game events and incorporates them into its responses
5. The agent can participate in a complete ECH0 game session, following the game's structure and contributing meaningfully to the narrative

## Initial Approach

Start by creating a minimal standalone test harness that can instantiate a Persona object from the original codebase, mocking the necessary dependencies (maze, other personas, etc.). This will allow us to understand the core cognitive loop and adapt it step by step for the TTRPG context.
