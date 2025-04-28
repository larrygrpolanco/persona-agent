# Project Brief: TTRPG Generative Agent

## Purpose
To design and implement a modular, LLM-driven generative agent architecture for use as a player or NPC in tabletop roleplaying games (TTRPGs), inspired by the "Generative Agents: Interactive Simulacra of Human Behavior" research. The agent will focus on narrative-driven cognition, memory, planning, and dialogue, enabling believable, context-aware roleplay in a story-driven environment.

## Core Goals
- Rebuild the generative agent architecture for narrative, not simulation.
- Enable agents to perceive, remember, plan, reflect, and act based on story context, not physical simulation.
- Support memory-driven dialogue, character development, and dynamic engagement with TTRPG scenes.
- Remove all simulation-specific logic (tiles, pathfinding, time-steps) and focus on narrative input/output.
- Provide robust LLM integration for all cognitive functions (perception, planning, reflection, conversation).
- Ensure extensibility for multi-agent play, campaign persistence, and integration with TTRPG systems.

## Scope
- Single and multi-agent support for TTRPGs (e.g., ECH0, custom games).
- Modular cognitive loop: Perceive → Retrieve → Plan → Reflect → Execute → Converse.
- Persistent memory (long-term and short-term) for narrative continuity.
- LLM-driven prompt engineering for all agent cognition.
- CLI or script-based test harness for agent interaction.

## Out of Scope
- Physical simulation, 2D/3D navigation, or time-stepped environments.
- Game engine or frontend integration (initially).
- Non-narrative agent behaviors (e.g., combat AI, rules arbitration).

## Success Criteria
- Agent can perceive narrative input, recall relevant memories, plan and reflect, and produce context-aware narrative actions and dialogue.
- Memory and cognition are transparent, extensible, and persistent.
- Architecture is documented and maintainable for future expansion.
