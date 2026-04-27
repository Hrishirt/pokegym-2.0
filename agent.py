import gymnasium as gym
import numpy as np
import time
from poke_env.player import Player
from poke_env.data import GenData


class agentPlayer(Player):
    
    @staticmethod
    def embed_battle(battle):
        # From the documentation
        # We will be using more features that are also not in the docs 
        # Currently thinking of using status conditions
        # Idea so far is to have switch features which track if our pokemon should swap 
        # The other feature are attacks features which track if our pokemon should attack and have a move selected
        base_power = -1 * np.ones(4)
        damage_multiplier = np.ones(4)
        best_pokemon = np.ones(6)
        active_matchup_score = 1
        