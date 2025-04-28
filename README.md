# TTRPG Agent Simulation Platform

A conversational agent system for role-playing game scenarios with autonomous character interactions.

## Quick Start

```bash
# 1. Clone repository (replace with your actual repo URL)
git clone https://github.com/larrygrpolanco/persona-agent.git
cd persona-agent

# 2. Install dependencies
python -m pip install -r requirements.txt

# Run with sample configurations (no installation needed)
python run.py ttrpg_agent/configs/pilot_config.json ttrpg_agent/configs/child*.json --cycles 3
```

## Key Features

- Character autonomy with memory persistence
- JSON-based configuration system
- CLI interface for scenario control
- Test suite with sample dialogues

## Command Reference

```bash
# Basic test run
python run.py [agent_configs] [options]

# Options:
# --cycles N      Number of interaction cycles (default: 3)
# --help          Show help message

# Example with custom configs:
python run.py path/to/your/*.json --cycles 5
```

## Project Structure
```
persona-agent/
├── ttrpg_agent/       # Core simulation engine
├── configs/           # Character personality templates
├── run.py             # Main execution script
└── memory-bank/       # Project documentation and context
```
