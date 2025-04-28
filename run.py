#!/usr/bin/env python3
import sys
import os

# Add parent directory to Python path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from ttrpg_agent.main import main

if __name__ == "__main__":
    main()
