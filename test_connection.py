import asyncio
from poke_env.player import RandomPlayer

async def main():
    player = RandomPlayer(
        battle_format="gen1randombattle",
        server_configuration=None,  # connects to localhost:8000 by default
        start_listening=False
    )
    print("Player created successfully")
    print(f"Username: {player.username}")

asyncio.run(main())