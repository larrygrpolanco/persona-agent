import json

class TTRPGAgent:
    """Core agent class for TTRPG characters"""
    
    def __init__(self, config_path):
        self.load_config(config_path)
        self.memories = []
        self.dialogue_history = []
        self.relationships = {}

    def load_config(self, config_path):
        """Load agent configuration from JSON file"""
        with open(config_path, 'r') as f:
            config = json.load(f)
            
        self.name = config['name']
        self.agent_type = config['type']
        self.background = config['background']
        self.relationships = config.get('relationships', {})
        
    def generate_response(self, other_agents, scene_context):
        """Generate dialogue response based on current state"""
        # Placeholder for LLM integration
        return f"{self.name}: Let's explore this together."
        
    def update_memories(self, interaction):
        """Record interactions in memory"""
        self.memories.append({
            'timestamp': len(self.memories),
            'interaction': interaction
        })
        
    def get_state(self):
        """Return current agent state snapshot"""
        return {
            'name': self.name,
            'type': self.agent_type,
            'memories': len(self.memories),
            'relationships': self.relationships
        }
