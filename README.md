# pokegym2

A Deep Reinforcement Learning agent that plays competitive Pokémon on a local Pokémon Showdown server, combining structured battle state with visual input from the battle screen.

## What This Is

pokegym2 is the successor to [pokegym](https://github.com/Hrishirt/pokegym) — a project that trained a PPO agent to beat Gym Leader Brock in FireRed by reading raw GBA memory. pokegym2 moves to a higher-level problem: competitive Pokémon with a full six-versus-six team, real type matchups, status conditions, and switching decisions.

The agent uses `poke-env` to interface with a local Pokémon Showdown server, receiving structured battle state every turn. The planned architecture combines this structured state with a CNN-processed visual observation of the battle screen — the same hybrid approach used in production game-playing agents like AlphaStar.

## Architecture (In Progress)

```
Local Showdown Server (Node.js)
        ↕  WebSocket (poke-env)
Battle State Parser
        ↕
Structured Observation          Visual Observation
(HP, types, moves, status)  +   (CNN on battle screenshot)
        ↕                               ↕
              Combined Feature Vector
                        ↕
              Deep RL Policy (PPO/DQN)
                        ↕
              Move Selection → Showdown
```

## Why Hybrid Observation?

Most Pokémon Showdown bots use only structured state — HP percentages, move names, type data. That information is clean and complete, but it misses what a human player sees: animation cues, HP bar colors, the visual rhythm of the battle.

By combining structured state with raw visual input, the agent can learn representations that neither input alone provides. This is the same design philosophy behind DeepMind's work on Atari and Blizzard games — structured game data augmented with pixels.

## Current Status

- [x] Local Showdown server running
- [x] Two random agents battling each other via poke-env
- [ ] Custom Gymnasium environment wrapping poke-env
- [ ] CNN visual encoder
- [ ] DQN/PPO training loop
- [ ] Benchmarking against RandomPlayer baseline

## Stack

- Python 3.11
- [poke-env](https://github.com/hsahovic/poke-env) — Pokémon Showdown Python interface
- [Pokémon Showdown](https://github.com/smogon/pokemon-showdown) — local battle server
- PyTorch — neural network and CNN encoder
- Stable Baselines3 — RL training
- Gymnasium — environment interface
- mss / pyautogui — screen capture for visual observations

## Setup

### Prerequisites
- Python 3.10+
- Node.js (for local Showdown server)

### 1. Start the local Showdown server

```bash
git clone https://github.com/smogon/pokemon-showdown.git
cd pokemon-showdown
npm install
node pokemon-showdown start --no-security
```

Server runs on `localhost:8000`.

### 2. Install Python dependencies

```bash
pip install poke-env stable-baselines3 torch gymnasium numpy
```

### 3. Test the connection

```bash
python test_connection.py
# Player created successfully
# Username: RandomPlayer 1
```

### 4. Run a test battle

```bash
python test_battle.py
# Two random agents fight on your local server
# Result prints to terminal
```

## Project Structure

```
pokegym2/
├── test_connection.py    # Verify poke-env connects to local server
├── test_battle.py        # Two random agents fight each other
├── env/
│   └── showdown_env.py   # Custom Gymnasium environment (coming)
├── agent/
│   └── rl_agent.py       # DQN/PPO agent (coming)
└── README.md
```

## Related Projects

**pokegym** — the predecessor to this project. A PPO agent that beats Gym Leader Brock in Pokémon FireRed by reading encrypted GBA RAM directly via a Lua TCP socket bridge. No type chart, no hardcoded rules — the agent discovers Water Gun beats Rock types through reward shaping alone.

→ [github.com/Hrishirt/pokegym](https://github.com/Hrishirt/pokegym)

## Citation

This project uses `poke-env` for interfacing with Pokémon Showdown:

```
@misc{poke_env,
    author       = {Haris Sahovic},
    title        = {Poke-env: pokemon AI in python},
    url          = {https://github.com/hsahovic/poke-env}
}
```

The local battle server is powered by the open-source [Pokémon Showdown](https://github.com/smogon/pokemon-showdown) project maintained by Smogon.
