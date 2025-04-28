import json
from ttrpg_agent.agent import TTRPGAgent

class Simulation:
    """Main simulation controller"""
    
    def __init__(self):
        self.agents = []
        self.scene_context = {}
        self.interaction_count = 0
        
    def load_agents(self, config_paths):
        """Initialize agents from config files"""
        for path in config_paths:
            agent = TTRPGAgent(path)
            self.agents.append(agent)
            
    def run_interaction_cycle(self):
        """Process one round of interactions between agents"""
        self.interaction_count += 1
        
        # Collect responses from all agents
        responses = []
        for agent in self.agents:
            other_agents = [a for a in self.agents if a != agent]
            response = agent.generate_response(other_agents, self.scene_context)
            responses.append(response)
            
            # Update memories for all other agents
            for other in other_agents:
                other.update_memories({
                    'from': agent.name,
                    'message': response,
                    'timestamp': self.interaction_count
                })
        
        return responses
    
    def get_snapshot(self):
        """Return current simulation state"""
        return {
            'interaction_count': self.interaction_count,
            'agents': [agent.get_state() for agent in self.agents],
            'scene': self.scene_context
        }
