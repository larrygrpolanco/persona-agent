#!/usr/bin/env python3
import argparse
import json
from ttrpg_agent.simulation import Simulation

def main():
    parser = argparse.ArgumentParser(description='Run TTRPG agent simulation')
    parser.add_argument('configs', nargs='+', help='Paths to agent config files')
    parser.add_argument('--cycles', type=int, default=3, help='Number of interaction cycles to run')
    
    args = parser.parse_args()
    
    # Initialize and run simulation
    sim = Simulation()
    sim.load_agents(args.configs)
    
    print(f"Running {args.cycles} interaction cycles...")
    for cycle in range(args.cycles):
        responses = sim.run_interaction_cycle()
        print(f"\n=== Cycle {cycle + 1} ===")
        for response in responses:
            print(response)
    
    print("\n=== Final State ===")
    print(json.dumps(sim.get_snapshot(), indent=2))

if __name__ == "__main__":
    main()
