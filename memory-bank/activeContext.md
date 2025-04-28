# Active Context: TTRPG Generative Agent

## Current Focus

We have completed the initial planning phase for the TTRPG Generative Agent project. We are now ready to implement Phase 1 (Memory Bank) and Phase 2 (Standalone Test Harness).

The Memory Bank (this documentation) provides a comprehensive understanding of the project goals, context, and technical approach. With this foundation in place, we can now focus on creating the standalone test harness that will allow us to instantiate and test a basic Persona agent outside of the original simulation environment.

## Active Decisions

1. **Minimal Modification Approach**: We've decided to initially modify the original codebase as little as possible, focusing on mocking dependencies rather than rewriting functionality. This will allow us to understand the core cognitive loop before making more substantial changes.

2. **Text-Based Input/Output**: The test harness will accept text input describing game events and produce text output representing the agent's responses. This replaces the spatial navigation and visual perception of the original system.

3. **Role-Based Initialization**: We will initialize the agent with either the Pilot or Child role from ECH0, providing appropriate initial memories and characteristics.

4. **Incremental Testing**: We will test each component of the cognitive loop individually before attempting to run the full cycle.

## Current Challenges

1. **Maze Dependency**: The original code relies heavily on the Maze class for perception and action. We need to create a comprehensive mock that provides the same interface but returns simplified data.

2. **Event Representation**: We need to determine how to represent narrative events in a format compatible with the existing memory structures.

3. **Planning Adaptation**: The original planning system is designed for daily schedules and physical actions. We need to adapt it for narrative contributions and dialogue.

4. **Reflection Triggers**: The original system triggers reflection based on importance thresholds of physical events. We need to adapt this for narrative contexts.

## Immediate Next Steps

1. **Create Project Structure**:
   ```
   ttrpg_agent/
   ├── persona/           # Copied from og-code/backend_server/persona/
   ├── mocks.py           # Mock implementations of dependencies
   └── test_harness.py    # Script to instantiate and test the agent
   ```

2. **Implement Mock Classes**:
   - `MockMaze`: Provides the same interface as the original Maze class but returns simplified data.
   - `MockPersonas`: A dictionary-like object that simulates other agents.
   - `MockTime`: A simple time management system to replace datetime handling.

3. **Adapt Persona Initialization**:
   - Modify the Persona class to accept a role parameter (Pilot/Child).
   - Create initial memories based on the role from ECH0.txt.
   - Initialize the agent with appropriate characteristics.

4. **Create Text Input Processing**:
   - Develop a function to convert text input into ConceptNode objects.
   - Bypass the spatial perception system in the perceive module.
   - Ensure events are properly stored in associative memory.

5. **Implement Basic Test Loop**:
   - Accept text input describing game events.
   - Process input through the cognitive cycle.
   - Generate and display agent responses.
   - Allow inspection of agent memory.

## Recent Learnings

1. The original architecture's memory retrieval system (combining recency, importance, and relevance) should work well for narrative contexts with minimal modification.

2. The reflection system, which creates higher-level insights from memories, will be particularly valuable for developing the agent's character over time.

3. The planning system will require the most significant adaptation, as it currently focuses on physical actions and locations rather than narrative contributions.

4. The original system's approach to conversation (in converse.py) may be directly applicable to TTRPG dialogue with minimal changes.

## Current Insights

1. **Memory is Key**: The memory stream is the most critical component to preserve, as it enables the agent to maintain consistency and develop over time.

2. **Reflection Drives Character**: The reflection system will be essential for developing the agent's understanding of its role and the narrative.

3. **Planning Needs Reimagining**: The planning system needs to be reimagined for narrative contexts, focusing on character goals and story contributions rather than physical actions.

4. **Perception is the Bridge**: The perception system is the main interface between the text-based TTRPG environment and the agent's internal cognitive processes.
