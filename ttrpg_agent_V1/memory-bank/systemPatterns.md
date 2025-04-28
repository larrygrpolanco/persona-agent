# System Patterns: TTRPG Generative Agent

## Original Architecture Overview

The Generative Agents architecture consists of three primary components that work together to create believable human-like behavior:

1. **Memory Stream**: A comprehensive record of the agent's experiences stored as natural language descriptions. Each memory includes:
   - A natural language description of an event/thought
   - Creation timestamp
   - Importance score ("poignancy")
   - Most recent access timestamp

2. **Retrieval System**: Selects relevant memories based on:
   - Recency: More recent memories are prioritized
   - Importance: More significant memories are prioritized
   - Relevance: Memories related to the current context are prioritized

3. **Reflection**: Periodically synthesizes memories into higher-level insights, creating a tree of reflections where:
   - Leaf nodes are direct observations
   - Non-leaf nodes are increasingly abstract thoughts
   - Reflections themselves become memories that can be retrieved

4. **Planning**: Creates and updates plans at multiple time scales:
   - High-level daily plans
   - Decomposed hourly activities
   - Minute-by-minute actions
   - Reactive adjustments based on unexpected events

## Key Architectural Challenges for TTRPG Adaptation

### 1. Replacing Spatial Grounding

The original architecture relied heavily on a 2D maze environment:
- Agents perceived nearby tiles and objects
- Actions were grounded in physical movement and object interaction
- The maze provided a shared objective reality for all agents

For our TTRPG agent, we need to replace this with:
- Text-based perception of narrative descriptions
- Actions expressed as dialogue or narrative contributions
- A shared understanding of the game state through text

### 2. Redefining "Events" and "Actions"

In the original system:
- Events were physical occurrences in the maze (e.g., "Isabella is making coffee")
- Actions were movements to locations and interactions with objects

In our TTRPG context:
- Events are narrative developments, dialogue, or descriptions
- Actions are verbal contributions to the story or game

### 3. Adapting the Planning System

The original planning system created daily schedules and decomposed them into specific actions. For TTRPGs:
- Instead of daily schedules, we need narrative goals and character motivations
- Instead of location-based planning, we need dialogue and story contribution planning
- Reactions need to be based on narrative developments rather than physical events

## Target TTRPG Agent Loop

```
┌─────────────────┐
│                 │
│  Text Input     │◄───────────────────┐
│  (Game State)   │                    │
│                 │                    │
└────────┬────────┘                    │
         │                             │
         ▼                             │
┌─────────────────┐                    │
│                 │                    │
│  Perceive       │                    │
│  (Parse Text)   │                    │
│                 │                    │
└────────┬────────┘                    │
         │                             │
         ▼                             │
┌─────────────────┐                    │
│                 │                    │
│  Retrieve       │                    │
│  Memories       │                    │
│                 │                    │
└────────┬────────┘                    │
         │                             │
         ▼                             │
┌─────────────────┐                    │
│                 │                    │
│  Plan Response  │                    │
│  or Action      │                    │
│                 │                    │
└────────┬────────┘                    │
         │                             │
         ▼                             │
┌─────────────────┐                    │
│                 │                    │
│  Generate       │                    │
│  Output Text    │                    │
│                 │                    │
└────────┬────────┘                    │
         │                             │
         ▼                             │
┌─────────────────┐                    │
│                 │                    │
│  Reflect        ├────────────────────┘
│  (Periodically) │
│                 │
└─────────────────┘
```

## Critical Implementation Paths

1. **Text Perception Module**:
   - Parse narrative text into structured events
   - Extract entities, actions, and relationships
   - Assign importance scores to events

2. **Memory Adaptation**:
   - Modify memory structures to handle narrative events
   - Adapt retrieval for TTRPG context relevance
   - Ensure reflections work with narrative rather than physical events

3. **Response Generation**:
   - Create in-character responses based on role (Pilot/Child)
   - Ensure responses reference relevant memories
   - Balance between advancing the narrative and staying in character

4. **Game State Tracking**:
   - Track the current phase of the ECH0 game
   - Maintain knowledge of introduced characters, locations, and objects
   - Understand the evolving relationship between the Pilot and Children

## Component Relationships

- **Memory Stream → Planning**: The agent's memories inform what kind of responses it generates, ensuring consistency with past events and character knowledge.

- **Planning → Output Generation**: The agent's plan for advancing the narrative guides the specific content of its responses.

- **Reflection → Memory Stream**: Periodic reflection creates higher-level understanding that gets stored back in memory, allowing the agent to develop its character over time.

- **Game State → Retrieval**: The current game state (e.g., which phase of ECH0) influences which memories are most relevant to retrieve.
