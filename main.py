import tkinter as tk
from tkinter import simpledialog

# Create the main application window
root = tk.Tk()
root.title("Conversation Viewer")
root.geometry("500x600")

# Prompt for participant names
participant1 = simpledialog.askstring("Participant", "Enter name of first participant (will appear on left):", parent=root)
participant2 = simpledialog.askstring("Participant", "Enter name of second participant (will appear on right):", parent=root)

# Create a frame to hold the conversation and scrollbar
main_frame = tk.Frame(root)
main_frame.pack(fill=tk.BOTH, expand=True)

# Create a canvas and scrollbar
canvas = tk.Canvas(main_frame, bg="white")
scrollbar = tk.Scrollbar(main_frame, orient="vertical", command=canvas.yview)
canvas.configure(yscrollcommand=scrollbar.set)

scrollbar.pack(side="right", fill="y")
canvas.pack(side="left", fill="both", expand=True)

# Create a frame inside the canvas to hold the messages
scrollable_frame = tk.Frame(canvas, bg="white")
scrollable_window = canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

# Update scrollregion when the size of the scrollable_frame changes
def on_frame_configure(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

scrollable_frame.bind("<Configure>", on_frame_configure)

# Resize the inner frame when the canvas size changes
def on_canvas_configure(event):
    canvas.itemconfig(scrollable_window, width=event.width)

canvas.bind("<Configure>", on_canvas_configure)

# Function to add a message bubble with side label and timestamp
def add_message(side, comment, timestamp):
    message_frame = tk.Frame(scrollable_frame, bg="white")
    message_frame.pack(anchor='w' if side == participant1 else 'e', pady=5, padx=10)

    side_label = tk.Label(message_frame, text=f"{side} [{timestamp}]", font=("Arial", 8, "bold"), bg="white")
    side_label.pack(anchor='w' if side == participant1 else 'e')

    bubble = tk.Label(message_frame, text=comment, bg="#E6E6E6" if side == participant1 else "#DCF8C6",
                      padx=10, pady=5, wraplength=300, justify=tk.LEFT if side == participant1 else tk.RIGHT)
    bubble.pack(anchor='w' if side == participant1 else 'e')

    # Auto-scroll to the bottom
    canvas.update_idletasks()
    canvas.yview_moveto(1.0)

# Function to prompt for input and add message
def prompt_and_add():
    side = simpledialog.askstring("Input", f"Enter side ({participant1}/{participant2}):", parent=root)
    comment = simpledialog.askstring("Input", "Enter comment:", parent=root)
    timestamp = simpledialog.askstring("Input", "Enter date and time (e.g., 2025-07-04 14:35 or July 4, 2025 2:35 PM):", parent=root)
    if side and comment and timestamp and side in [participant1, participant2]:
        add_message(side, comment, timestamp)

# Button to add a new message
add_button = tk.Button(root, text="Add Message", command=prompt_and_add)
add_button.pack(pady=10)

# Start the GUI event loop
root.mainloop()
