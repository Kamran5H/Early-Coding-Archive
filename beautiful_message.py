import tkinter as tk

# The message lines and their emojis
lines = [
    "You say you're okay 😐,",
    "But You're not 😔",
    "Please naa.. 🙏",
    "I'm insaan bna hua 🧑",
    "And I'm Missing you A lot 😢💔",
    "AB dekhein ap ne 10:43 wala time b guzaar dia ⏰",
    "much bol dete USS time to shaayed muje lgta k ap maan gye hein 🤔",
    "but I know , ni maane tussi 🥺"
]

# Colors for each line (feel free to adjust to your taste)
colors = [
    "#0033cc",  # Blue
    "#a020f0",  # Purple
    "#ff9900",  # Orange
    "#009900",  # Green
    "#ff3333",  # Red
    "#e67e22",  # Carrot orange
    "#16a085",  # Teal
    "#e84393"   # Pink
]

# Create the main window
root = tk.Tk()
root.title("Beautiful Message")
root.configure(bg='white')

# Make window fullscreen
root.state('zoomed')

# Use a frame to center the labels vertically and horizontally
frame = tk.Frame(root, bg='white')
frame.pack(expand=True)

# Font settings
font_family = "Segoe UI Emoji"
font_size = 36
font_weight = "bold"

# Add each line as a label
for idx, line in enumerate(lines):
    label = tk.Label(
        frame,
        text=line,
        font=(font_family, font_size, font_weight),
        fg=colors[idx % len(colors)],
        bg='white',
        anchor='center'
    )
    label.pack(pady=6)  # Space between lines

root.mainloop()