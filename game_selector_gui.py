import os
import subprocess
import shlex
import tkinter as tk
from tkinter import PhotoImage, Label, Toplevel, font
from PIL import Image, ImageTk

# Function to list available games in the current directory and its subdirectories


def list_available_games():
    games = []
    for root, _, files in os.walk('.'):
        if 'venv' in root:
            continue
        for file in files:
            if file.endswith('.py') and file not in ['game_selector.py', 'base.py', 'bird.py', 'neat.py', 'pipe.py', 'my_neat.py']:
                games.append(os.path.join(root, file))
    return games

# Function to run the selected game


def run_game(game_file):
    try:
        command = ['python'] + shlex.split(f'"{game_file}"')
        subprocess.call(command)
    except subprocess.CalledProcessError as e:
        print(f"Error while running the game: {e}")

# Function to handle hover effect


def on_hover(e, label, original_image, original_pil_image):
    # Resize the image to 300x300 when hovering
    hover_pil_image = original_pil_image.resize((250, 250), Image.ANTIALIAS)
    hover_image = ImageTk.PhotoImage(hover_pil_image)
    label.config(image=hover_image)
    label.image = hover_image  # Keep a reference to prevent garbage collection


def on_leave(e, label, original_image, original_pil_image):
    label.config(image=original_image)

# Function to create game icons


def create_game_icons(root, games):

    # Create a cool label at the top
    cool_font = font.Font(family="Helvetica", size=36, weight="bold")
    title_label = Label(root, text="PyGame Arcade", font=cool_font, fg="blue")
    # Add some padding to move it away from the top edge
    title_label.pack(pady=120)

    # Create a frame to hold the game icons
    frame = tk.Frame(root)
    # Add some vertical padding between the label and the images
    frame.pack()

    for game in games:
        # Remove the '.py' extension from the game filename
        game_name = os.path.splitext(os.path.basename(game))[0]

        # Load both the original and hover images (assuming PNG format)
        try:
            if game_name == 'cube_game' or game_name == 'flappy_main' or game_name == 'pong' or game_name == 'snake_game' or game_name == 'pipe':
                # Open the image using PIL
                original_pil_image = Image.open(f"{game_name}.png")

                # Resize the image
                resized_pil_image = original_pil_image.resize(
                    (200, 200), Image.ANTIALIAS)

                # Convert the PIL image to a PhotoImage object
                original_image = ImageTk.PhotoImage(resized_pil_image)

                # hover_image = PhotoImage(file=f"{game_name}_hover.png")
            else:
                continue
        except tk.TclError as e:
            print(f"Error loading images for {game_name}: {e}")
            continue

        # Create a label with the image
        label = Label(frame, image=original_image)
        label.image = original_image

        # Add padding for spacing between images
        label.pack(side=tk.LEFT, padx=20, pady=20)

        label.bind("<Enter>", lambda e, label=label, original_image=original_image,
                   original_pil_image=original_pil_image: on_hover(e, label, original_image, original_pil_image))
        label.bind("<Leave>", lambda e, label=label, original_image=original_image,
                   original_pil_image=original_pil_image: on_leave(e, label, original_image, original_pil_image))

        # Bind the click event to run the game
        label.bind("<Button-1>", lambda e, game=game: run_game(game))

# Main function to create the Tkinter window


def main():
    root = tk.Tk()
    root.title("PyGame Arcade")
    root.geometry("1000x800")

    games = list_available_games()
    create_game_icons(root, games)

    root.mainloop()


if __name__ == '__main__':
    main()
