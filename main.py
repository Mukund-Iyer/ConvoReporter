import tkinter as tk
from tkinter import simpledialog, filedialog, messagebox
from datetime import datetime
import json

# Create the main application window
root = tk.Tk()
root.title("Conversation Reporter")
root.geometry("500x600")

# Initialize participant variables
participant1 = None
participant2 = None
left_participant = None
right_participant = None

# Store messages
conversation = []

# Create a frame to hold the conversation and scrollbar
main_frame = tk.Frame(root)
main_frame.pack(fill=tk.BOTH, expand=True)

canvas = tk.Canvas(main_frame, bg="white")
scrollbar = tk.Scrollbar(main_frame, orient="vertical", command=canvas.yview)
canvas.configure(yscrollcommand=scrollbar.set)

scrollbar.pack(side="right", fill="y")
canvas.pack(side="left", fill="both", expand=True)

scrollable_frame = tk.Frame(canvas, bg="white")
scrollable_window = canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

def on_frame_configure(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

scrollable_frame.bind("<Configure>", on_frame_configure)

def on_canvas_configure(event):
    canvas.itemconfig(scrollable_window, width=event.width)

canvas.bind("<Configure>", on_canvas_configure)

def render_conversation():
    for widget in scrollable_frame.winfo_children():
        widget.destroy()

    sorted_convo = sorted(conversation, key=lambda x: x["parsed_time"])

    for msg in sorted_convo:
        side = msg["side"]
        comment = msg["comment"]
        timestamp = msg["timestamp"]
        align = 'w' if side == left_participant else 'e'

        message_frame = tk.Frame(scrollable_frame, bg="white")
        message_frame.pack(anchor=align, pady=5, padx=10)

        side_label = tk.Label(message_frame, text=f"{side} [{timestamp}]", font=("Arial", 8, "bold"), bg="white")
        side_label.pack(anchor=align)

        bubble = tk.Label(message_frame, text=comment,
                          bg="#E6E6E6" if side == left_participant else "#DCF8C6",
                          padx=10, pady=5, wraplength=300,
                          justify=tk.LEFT if side == left_participant else tk.RIGHT)
        bubble.pack(anchor=align)

    canvas.update_idletasks()
    canvas.yview_moveto(1.0)

def add_message(side, comment, timestamp):
    try:
        parsed_time = datetime.strptime(timestamp, "%d-%m-%Y %H:%M")
    except ValueError:
        messagebox.showerror("Invalid Timestamp", "Please use format: DD-MM-YYYY HH:MM")
        return

    conversation.append({
        "side": side,
        "comment": comment,
        "timestamp": timestamp,
        "parsed_time": parsed_time
    })

    render_conversation()

def prompt_and_add():
    global participant1, participant2, left_participant, right_participant

    if not participant1 or not participant2:
        participant1 = simpledialog.askstring("Participant", "Enter name of first participant:", parent=root)
        participant2 = simpledialog.askstring("Participant", "Enter name of second participant:", parent=root)
        if not participant1 or not participant2:
            messagebox.showwarning("Missing Info", "Both participant names are required.")
            return
        left_participant, right_participant = sorted([participant1, participant2])

    side = simpledialog.askstring("Input", f"Enter side ({participant1}/{participant2}):", parent=root)
    comment = simpledialog.askstring("Input", "Enter comment:", parent=root)
    timestamp = simpledialog.askstring("Input", "Enter date and time (e.g., 04-07-2025 14:35):", parent=root)
    if side and comment and timestamp and side in [participant1, participant2]:
        add_message(side, comment, timestamp)

def export_conversation():
    file_path = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON files", "*.json")])
    if file_path:
        export_data = [
            {"side": msg["side"], "comment": msg["comment"], "timestamp": msg["timestamp"]}
            for msg in conversation
        ]
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(export_data, f, indent=4)
        messagebox.showinfo("Export", "Conversation exported successfully!")

def import_conversation():
    global participant1, participant2, left_participant, right_participant

    file_path = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
    if file_path:
        with open(file_path, "r", encoding="utf-8") as f:
            imported = json.load(f)

        if not participant1 or not participant2:
            participant_list = []
            for instance in imported:
                if instance["side"] not in participant_list:
                    participant_list.append(instance["side"])

            left_participant, right_participant = sorted(participant_list)
            participant1, participant2 = sorted(participant_list)

        for msg in imported:
            add_message(msg["side"], msg["comment"], msg["timestamp"])

        messagebox.showinfo("Import", "Conversation imported successfully!")

# Create a menu bar
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# Create a "File" menu
file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)

file_menu.add_command(label="Add Message", command=prompt_and_add)
file_menu.add_command(label="Export Conversation", command=export_conversation)
file_menu.add_command(label="Import Conversation", command=import_conversation)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

# Start the GUI event loop
root.mainloop()
