# Technical Context: TTRPG Generative Agent

## Technology Stack

### Programming Language
- **Python**: The project will be implemented in Python, maintaining consistency with the original codebase.

### External Dependencies
- **Large Language Models (LLMs)**: The original architecture relies heavily on LLMs (specifically ChatGPT/GPT-3.5-turbo) for generating natural language responses, reflections, and plans. We will maintain this dependency.
- **Vector Embeddings**: Used for memory retrieval based on semantic similarity.

### Source Codebase
- **Original Repository**: `og-code/backend_server/` contains the core implementation of the Generative Agents architecture.
- **Key Files**:
  - `og-code/backend_server/reverie.py`: The main orchestration file for the simulation.
  - `og-code/backend_server/persona/persona.py`: The core Persona class that implements the agent.
  - `og-code/backend_server/persona/memory_structures/`: Contains implementations of memory systems.
  - `og-code/backend_server/persona/cognitive_modules/`: Contains implementations of cognitive functions.
  - `og-code/backend_server/persona/prompt_template/`: Contains LLM prompts for various agent functions.

### Target Game
- **ECH0**: A GM-less storytelling game defined in `ECH0.txt`. This provides the rules and structure for our agent to operate within.

## Technical Constraints

### Removing Simulation Dependencies
The original codebase is deeply integrated with a 2D simulation environment:
- **Maze**: A 2D grid environment that agents navigate.
- **Time Stepping**: The simulation advances in discrete time steps.
- **Multi-Agent Coordination**: Agents interact with each other through the shared environment.

These dependencies need to be removed or mocked to create a standalone agent.

### LLM Limitations
- **Context Window**: LLMs have limited context windows, requiring careful management of what information is included in prompts.
- **Determinism**: LLM outputs can vary, potentially causing inconsistent agent behavior.
- **Cost and Latency**: API calls to LLMs incur costs and introduce latency, requiring efficient use.

## Development Approach

### Phase 1: Standalone Test Harness
1. **Copy Core Code**: Extract the `persona/` directory from the original codebase.
2. **Mock Dependencies**: Create mock implementations of the Maze and other simulation components.
3. **Adapt Interfaces**: Modify the Persona class to accept text input instead of simulation state.
4. **Minimal Viable Agent**: Create a simple test harness that can instantiate a Persona and run its cognitive cycle.

### Phase 2: TTRPG Adaptation
1. **Text Perception**: Replace the spatial perception system with text parsing.
2. **Role Definition**: Implement the Pilot and Child roles from ECH0.
3. **Game State Tracking**: Create a system to track the current state of the ECH0 game.
4. **Response Generation**: Adapt the planning and execution systems to generate appropriate in-character responses.

### Phase 3: Refinement and Testing
1. **Memory Tuning**: Adjust importance scoring and retrieval for narrative contexts.
2. **Reflection Enhancement**: Improve reflection to focus on character development and narrative understanding.
3. **End-to-End Testing**: Test the agent in complete ECH0 game sessions.

## Tool Usage Patterns

### Memory Structures
- **Associative Memory (`a_mem`)**: Stores events, thoughts, and conversations as `ConceptNode` objects.
- **Spatial Memory (`s_mem`)**: Originally stored knowledge of the physical environment; will need adaptation for narrative environments.
- **Scratch (`scratch`)**: Stores transient information about the agent's current state.

### Cognitive Modules
- **Perceive**: Processes input to create memory entries.
- **Retrieve**: Selects relevant memories based on the current context.
- **Plan**: Determines what the agent should do next.
- **Reflect**: Synthesizes memories into higher-level insights.
- **Execute**: Translates plans into concrete actions.
- **Converse**: Manages conversations with other agents or players.

### LLM Prompting
The system uses carefully crafted prompts to elicit specific behaviors from the LLM:
- **Few-shot examples**: Demonstrate desired outputs.
- **Structured formats**: Ensure consistent parsing of LLM responses.
- **Character context**: Include relevant agent memories and traits.

## Technical Risks and Mitigations

### Risk: Deep Integration with Maze
**Mitigation**: Create a comprehensive mock that provides the same interface but returns simplified data.

### Risk: Complex Interdependencies Between Components
**Mitigation**: Start with a minimal implementation and incrementally add features, testing at each step.

### Risk: LLM Costs
**Mitigation**: Implement caching for common queries and optimize prompt design to reduce token usage.

### Risk: Maintaining Character Consistency
**Mitigation**: Enhance the reflection system to periodically reinforce character traits and motivations.
