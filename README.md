# Bowling Game API and Simulation

## Overview
This project provides an API for managing a bowling game, including scoring, recording rolls, and retrieving game details. It also includes a Python-based graphical simulation using Pygame where users can input player details, simulate rolls, and view game progress.

The API supports standard bowling rules, where a game consists of 10 frames, and players can have up to two rolls per frame, with special rules for the 10th frame.

## Features
- **Create Game**: Set up a new game with specified player details and configurations.
- **Record Rolls**: Log each player's roll in the game.
- **Game Details**: Retrieve scores and other details of a game.
- **Historical Performance**: Access historical game data for each player.
- **Graphical Simulation**: Run a graphical interface to simulate the bowling rolls and scoring.

## Installation

To get started, clone the repository and install the required dependencies.

```bash
git clone https://github.com/yourusername/bowling-game-api.git
cd bowling-game-api
pip install -r requirements.txt
```

## Usage

### Running the API Server
To start the API server, run the following command from the root directory of the project:

```bash
uvicorn main:app --reload
```
This will start the API server on `http://127.0.0.1:8000`. You can access the API documentation at `http://127.0.0.1:8000/docs`.

### Running the Bowling Simulation
To start the bowling simulation, ensure you have Pygame installed and run:

```bash
python simulation.py
```

### API Endpoints

- `POST /games/`: Create a new game.
  - **Parameters**:
    - `date`: Date and time the game is created.
    - `game_type`: Type of game (e.g., "League", "Practice").
    - `lane_number`: Bowling lane number.
    - `players`: List of players participating.
    - `frames`: Number of frames (default is 10).
    - `format`: Game format ("standard" or "custom").
  
- `POST /games/{game_id}/rolls`: Record a roll for a specific game.
  - **Parameters**:
    - `game_id`: Unique identifier for the game.
    - `player_id`: ID of the player making the roll.
    - `frame_number`: Current frame number.
    - `roll_number`: Roll number within the frame.
    - `pins_knocked_down`: Number of pins knocked down in the roll.

- `GET /games/{game_id}/details`: Get detailed information about a game, including all rolls and players.
  - **Parameters**:
    - `game_id`: Unique identifier for the game.

- `GET /games/{game_id}/score`: Retrieve the current score for a game.
  - **Parameters**:
    - `game_id`: Unique identifier for the game.

- `GET /games/{game_id}/summary`: Get a natural language summary of the current game state.
  - **Parameters**:
    - `game_id`: Unique identifier for the game.

### Example Requests
```bash
# Create a new game
curl -X 'POST' \
  'http://127.0.0.1:8000/games/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "date": "2024-10-20T12:00:00",
  "game_type": "League",
  "lane_number": 1,
  "players": [
    {"name": "John Doe", "skill_level": "experienced"},
    {"name": "Jane Doe", "skill_level": "beginner"}
  ],
  "frames": 10,
  "format": "standard"
}'
```

## Contributing
Contributions are welcome! For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)
