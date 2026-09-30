import tkinter as tk

# Your message broken into lines with relevant emojis
lines = [
    "Boss, I've learned thori c Python aj 😎🐍",
    "to kuch task , ya assignment to dein 📝",
    "Taa k test Pta chle zra 🔥🤓"
]

# Beautiful, vivid colors for each line
colors = [
    "#e17055",  # vibrant red-orange
    "#0984e3",  # bright blue
    "#00b894"   # vivid green
]

# Create main window
root = tk.Tk()
root.title("Python Assignment Request")
root.configure(bg='white')
root.state('zoomed')  # Fullscreen (use root.attributes('-fullscreen', True) for true fullscreen)

# Frame to center everything
frame = tk.Frame(root, bg='white')
frame.pack(expand=True)

# Font settings
font_family = "Segoe UI Emoji"
font_size = 44
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
    label.pack(pady=16)  # Space between lines for visibility

root.mainloop()