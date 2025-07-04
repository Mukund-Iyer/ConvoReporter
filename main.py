import tkinter as tk
from tkinter import simpledialog

# Create the main application window
root = tk.Tk()
root.title("Conversation Viewer")
root.geometry("500x600")

# Prompt for participant names
participant1 = simpledialog.askstring("Participant", "Enter name of first participant (will appear on left):", parent=root)
participant2 = simpledialog.askstring("Participant", "Enter name of second participant (will appear on right):", parent=root)

# Create a frame to hold the conversation
conversation_frame = tk.Frame(root, bg="white")
conversation_frame.pack(fill=tk.BOTH, expand=True)

# Function to add a message bubble with side label
def add_message(side, comment):
    message_frame = tk.Frame(conversation_frame, bg="white")
    message_frame.pack(anchor='e' if side == participant2 else 'w', pady=5, padx=10, fill=tk.X)

    side_label = tk.Label(message_frame, text=side, font=("Arial", 8, "bold"), bg="white", anchor='w')
    side_label.pack(anchor='w' if side == participant1 else 'e')

    bubble = tk.Label(message_frame, text=comment, bg="#DCF8C6" if side == participant2 else "#E6E6E6",
                      padx=10, pady=5, wraplength=300, justify=tk.LEFT if side == participant1 else tk.RIGHT)
    bubble.pack(anchor='e' if side == participant2 else 'w')

# Function to prompt for input and add message
def prompt_and_add():
    side = simpledialog.askstring("Input", f"Enter side ({participant1}/{participant2}):", parent=root)
    comment = simpledialog.askstring("Input", "Enter comment:", parent=root)
    if side and comment and side in [participant1, participant2]:
        add_message(side, comment)

# Button to add a new message
add_button = tk.Button(root, text="Add Message", command=prompt_and_add)
add_button.pack(pady=10)

# Start the GUI event loop
root.mainloop()
