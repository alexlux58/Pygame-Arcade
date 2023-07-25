import argparse
import os
import subprocess


def list_available_games():
    games = []
    for root, _, files in os.walk('.'):
        for file in files:
            if file.endswith('.py') and file != 'game_selector.py' and not file.startswith('_') and file != 'base.py' and file != 'bird.py' and file != 'neat.py' and file != 'pipe.py':
                games.append(os.path.join(root, file))
    return games


def run_game(game_file):
    if not game_file.endswith('.py'):
        print("Invalid game file format. Please provide a .py file.")
        return

    if not os.path.isfile(game_file):
        print(f"Game file '{game_file}' not found.")
        return

    try:
        subprocess.run(['python', game_file], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error while running the game: {e}")
    except KeyboardInterrupt:
        print("\nGame selection cancelled.")


def main():
    parser = argparse.ArgumentParser(
        description="Select and run Python games.")
    parser.add_argument('-l', '--list', action='store_true',
                        help="List available games.")
    parser.add_argument('-g', '--game', metavar='game.py',
                        type=str, help="Run the selected game.")

    args = parser.parse_args()

    if args.list:
        print("Available games:")
        games = list_available_games()
        for idx, game in enumerate(games, 1):
            print(f"{idx}. {game}")
        return

    if args.game:
        run_game(args.game)
        return

    # Check if the user wants to run Flappy Bird
    flappy_main_path = os.path.join("FlappyBirdWithAI", "flappy_main.py")
    if os.path.exists(flappy_main_path):
        print("Running Flappy Bird...")
        try:
            subprocess.run(['python', flappy_main_path],
                           check=True, cwd="FlappyBirdWithAI")
        except subprocess.CalledProcessError as e:
            print(f"Error while running the game: {e}")
        except KeyboardInterrupt:
            print("\nGame selection cancelled.")
    else:
        print("Flappy Bird not found. Please make sure it exists in the 'FlappyBirdWithAI' directory.")


if __name__ == '__main__':
    main()
