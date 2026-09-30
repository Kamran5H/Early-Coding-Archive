from rich.console import Console
from rich.text import Text
import pyfiglet
import time
import os

# Prepare the message and emojis
lines = [
    "You say you're okay 😐,",
    "But You're not 😔",
    "Please naa.. 🙏",
    "I'm insaan bna hua 🧑",
    "And I'm Missing you Laot 😢💔",
]

# Define colors for each line
colors = ["cyan", "magenta", "yellow", "green", "red"]

# Clear the screen
os.system('cls' if os.name == 'nt' else 'clear')

console = Console()

# Print each line in big ASCII art with color and emoji
for idx, line in enumerate(lines):
    fig = pyfiglet.figlet_format(line, font="slant")
    text = Text(fig, style=colors[idx % len(colors)])
    console.print(text)
    time.sleep(0.5)  # Pause for dramatic effect

# Keep the screen until user closes the window
input("\nPress Enter to exit...")