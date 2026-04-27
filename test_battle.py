import asyncio
from poke_env import AccountConfiguration
from poke_env.player import RandomPlayer

def create_player(name):
    my_character_config = AccountConfiguration(name, None)
    print(my_character_config)
    # player = RandomPlayer(account_configuration=my_character_config)
    return my_character_config


async def main():
    player_1_config = create_player("Israfils")
    player_1 = RandomPlayer(account_configuration=player_1_config, max_concurrent_battles=1)
    player_2 = RandomPlayer(max_concurrent_battles=1)

    await player_1.battle_against(player_2, n_battles=1)
    if player_1.battles:
        battle = list(player_1.battles.values())[0]
        
        # Check if the battle has a 'last_request' attribute
        if hasattr(battle, "last_request"):
            print("--- Available Moves from Last Request ---")
            print(battle.last_request)
        
        # Access moves via the 'available_moves' list directly
        print("\n--- Parsed Moves ---")
        for move in battle.available_moves:
            print(f"Move: {move.id} | Base Power: {move.base_power}")
    else:
        print("No battles found in player history.")


    team = battle.last_request['side']['pokemon']

    for mon in team:
        print(f"Pokémon: {mon['ident']}")
        print(f"Moves: {mon['moves']}")
    
    for mon_id, mon in battle.opponent_team.items():
        print(f"Opponent Mon: {mon.species}")
        print(f"Types: {mon.type_1}, {mon.type_2}")
if __name__ == "__main__":
    asyncio.run(main())