from ttrpg_agent.simulation import Simulation

def run_test():
    # Initialize simulation
    sim = Simulation()
    
    # Load agent configurations
    configs = [
        "configs/pilot_config.json",
        "configs/child1_config.json",
        "configs/child2_config.json"
    ]
    sim.load_agents(configs)
    
    # Run 3 interaction cycles
    for cycle in range(3):
        print(f"\n=== Interaction Cycle {cycle + 1} ===")
        responses = sim.run_interaction_cycle()
        for response in responses:
            print(response)
    
    # Show final state
    print("\n=== Final Simulation State ===")
    print(sim.get_snapshot())

if __name__ == "__main__":
    run_test()
