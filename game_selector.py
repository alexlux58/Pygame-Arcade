# Import necessary modules
import argparse
import os
import subprocess
import shlex

# Function to list available games in the current directory and its subdirectories


def list_available_games():
    games = []
    # os.walk() generates the file names in a directory tree
    for root, _, files in os.walk('.'):
        # Check if the current directory is the 'venv' directory
        if 'venv' in root:
            continue
        for file in files:
            # Check if the file has a .py extension and is not one of the excluded files
            if file.endswith('.py') and file != 'game_selector.py' and not file.startswith('_') and file != 'base.py' and file != 'bird.py' and file != 'neat.py' and file != 'pipe.py' and file != 'my_neat.py':
                # Append the full path of the game file to the list of games
                games.append(os.path.join(root, file))
    return games

# Function to run the selected game


def run_game(game_file):
    # Check if the provided file has a .py extension
    if not game_file.endswith('.py'):
        print("Invalid game file format. Please provide a .py file.")
        return

    # Check if the file exists in the current directory or its subdirectories
    if not os.path.isfile(game_file):
        print(f"Game file '{game_file}' not found.")
        return

    try:
        # Manually split the command into individual arguments
        command = ['python'] + shlex.split(f'"{game_file}"')
        # Run the selected game using the 'subprocess' module
        subprocess.call(command)
    except subprocess.CalledProcessError as e:
        print(f"Error while running the game: {e}")
    except KeyboardInterrupt:
        print("\nGame selection cancelled.")

# Main function


def main():
    # Create a parser to handle command-line arguments
    parser = argparse.ArgumentParser(
        description="Select and run Python games.")
    parser.add_argument('-l', '--list', action='store_true',
                        help="List available games.")
    parser.add_argument('-g', '--game', metavar='game.py',
                        type=str, help="Run the selected game.")

    # Parse the command-line arguments
    args = parser.parse_args()

    # If the '-l' or '--list' option is provided, list available games and exit
    if args.list:
        print("Available games:")
        games = list_available_games()
        for idx, game in enumerate(games, 1):
            print(f"{idx}. {game}")
        return

    # If the '-g' or '--game' option is provided, run the selected game
    if args.game:
        run_game(args.game)
        return

    # If no options are provided, check if the user wants to run Flappy Bird
    flappy_main_path = os.path.join("FlappyBirdWithAI", "flappy_main.py")
    if os.path.exists(flappy_main_path):
        print("Running Flappy Bird...")
        try:
            # Run Flappy Bird using 'subprocess' with the appropriate working directory
            subprocess.run(['python', flappy_main_path],
                           check=True, cwd="FlappyBirdWithAI")
        except subprocess.CalledProcessError as e:
            print(f"Error while running the game: {e}")
        except KeyboardInterrupt:
            print("\nGame selection cancelled.")
    else:
        print("Flappy Bird not found. Please make sure it exists in the 'FlappyBirdWithAI' directory.")


# Entry point of the script
if __name__ == '__main__':
    main()
