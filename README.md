# Game Selector

This script allows you to select and run Python games from a list of available options. It provides a simple command-line interface to interact with the games.

## Requirements

- Python 3.x

## Usage

Run the script with the desired command-line arguments to list available games or run a specific game.

`python game_selector.py [-h] [-l] [-g game.py]`

### Command-line Arguments

- `-h`, `--help`: Show the help message and exit.
- `-l`, `--list`: List available games.
- `-g game.py`, `--game game.py`: Run the selected game.

## List Available Games

You can list all the available games by using the `-l` or `--list` option. The script will traverse through the current directory and its subdirectories to find games with the '.py' extension. Games that should not be listed (e.g., 'game_selector.py', 'base.py', 'bird.py', 'neat.py', 'pipe.py') are excluded.

`python game_selector.py -l`

## Run a Game

To run a specific game, use the `-g` or `--game` option followed by the filename of the game you want to play. The game file should be in the '.py' format.

`python game_selector.py -g game.py`

## Running Flappy Bird

If you want to run Flappy Bird, the script will attempt to execute it from the 'FlappyBirdWithAI' directory. If the game file 'flappy_main.py' is found, it will be launched.

Note: Ensure that 'FlappyBirdWithAI' and 'flappy_main.py' exist in the specified directory.

`python game_selector.py`

## Example

List available games:

`python game_selector.py -l`

Run a specific game (replace `game.py` with the actual filename of the game you want to play):

`python game_selector.py -g game.py`

Run Flappy Bird (if available):

`python game_selector.py`

## Note

This script relies on the `subprocess` module to execute the games, and it expects the games to be implemented as standalone Python scripts with a '.py' extension.
