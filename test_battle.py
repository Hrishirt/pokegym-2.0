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

    print(f"Finished battles: {player_1.n_finished_battles}")
    print(f"Player 1 wins: {player_1.n_won_battles}")


if __name__ == "__main__":
    asyncio.run(main())