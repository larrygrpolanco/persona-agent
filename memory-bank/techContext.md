# Tech Context: TTRPG Generative Agent

## Technologies Used
- **Python 3.x**: Primary language for all agent logic and orchestration.
- **OpenAI GPT APIs**: For all LLM-driven cognition (dialogue, planning, reflection, etc.).
- **NumPy**: For embedding similarity and vector operations.
- **File System (JSON/CSV)**: For persistent memory, agent state, and campaign data.
- **Prompt Templates (Text Files)**: For modular, reusable LLM prompt engineering.

## Development Setup
- Modular Python package structure for agent, memory, cognitive modules, and prompt infrastructure.
- CLI or script-based test harness for agent interaction and debugging.
- Memory Bank (Markdown) for project documentation and context continuity.

## Technical Constraints
- No simulation engine, tile-based navigation, or real-time environment.
- All agent cognition and action must be narrative-driven and LLM-compatible.
- Must support persistent, inspectable memory for campaign continuity.
- Designed for extensibility: new prompt types, memory structures, or cognitive modules can be added as needed.

## Dependencies
- openai (Python package)
- numpy
- (Optional) tiktoken or other tokenizer for prompt management
- Standard Python libraries: os, sys, json, csv, datetime, etc.

## Tool Usage Patterns
- All LLM calls are routed through robust API wrappers with validation and retry logic.
- Embeddings are generated for all memory nodes to enable semantic retrieval.
- Prompt templates are loaded and filled dynamically for each cognitive function.
- File/folder utilities are used for saving/loading agent state and campaign data.

## Future Considerations
- Potential for API/server-based deployment for integration with chat platforms or VTTs.
- Support for additional LLM providers or local models.
- Optional frontend or GM/DM console for campaign management.
