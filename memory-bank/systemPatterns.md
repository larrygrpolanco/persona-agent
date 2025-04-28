# System Patterns: TTRPG Generative Agent

## System Architecture
- **Modular Cognitive Loop:** The agent is structured around a modular cognitive loop: Perceive → Retrieve → Plan → Reflect → Execute → Converse.
- **Memory-Driven Behavior:** All agent actions, dialogue, and planning are informed by persistent associative (long-term) and scratch (short-term) memory.
- **LLM Integration:** All cognition is LLM-driven, with prompt engineering and embedding-based retrieval for context-aware responses.

## Key Technical Decisions
- **Narrative-First Design:** All simulation-specific logic (tiles, pathfinding, time-steps) is removed. The agent operates purely on narrative input and output.
- **Prompt-Oriented Modules:** Each cognitive function (planning, reflection, conversation, etc.) is implemented as a prompt-oriented module, using reusable templates and robust LLM API wrappers.
- **Semantic Memory Retrieval:** Embedding-based similarity is used to retrieve relevant memories, supporting continuity and context in narrative play.
- **Extensible World Knowledge:** (Optional) Hierarchical world knowledge tree for tracking narrative locations, objects, and facts.

## Design Patterns
- **Separation of Concerns:** Each cognitive module is independent and interacts via well-defined interfaces.
- **Persistence:** All agent state (memory, identity, narrative state) is serializable for campaign continuity.
- **Transparency:** Memory and reasoning are inspectable for debugging, GM oversight, or player transparency.
- **Extensibility:** The architecture supports adding new cognitive modules, prompt types, or memory structures as needed.

## Critical Implementation Paths
- **Perception:** Narrative input parsing and event extraction.
- **Memory Retrieval:** Weighted combination of recency, importance, and semantic similarity.
- **Planning/Reflection:** LLM-driven generation of narrative actions, goals, and character development.
- **Dialogue:** Multi-turn, memory-driven conversation with relationship and idea summarization.

## Component Relationships
- **Persona Orchestrator:** Wires together all cognitive modules and manages agent state.
- **Cognitive Modules:** Each module (perceive, retrieve, plan, reflect, execute, converse) is responsible for a distinct aspect of agent cognition.
- **Prompt Infrastructure:** Centralizes all LLM interaction and prompt engineering.
- **Memory System:** Provides persistent, queryable storage for all agent experiences and state.
