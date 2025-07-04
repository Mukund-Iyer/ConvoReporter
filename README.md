# 🗨️ Conversation Reporter
A simple Tkinter-based GUI application that allows users to simulate and view a two-person conversation with custom messages, timestamps, and dates. 
This application is still under progress and requires more work to be done. Ultimate aim is to extract stuff from Outlook and put it here as a conversation.

## 📋 Features
- Prompt users to enter names for two participants.
- Display messages in a chat-style interface with:
  - Left/right alignment based on the speaker.
  - Colored message bubbles.
  - Custom date and time for each message.
- Scrollable conversation window.
- Easy-to-use message input via dialog boxes.

## 🖼️ Interface
- **Left side**: Messages from Participant 1.
- **Right side**: Messages from Participant 2.
- Each message includes:
  - The participant's name.
  - A user-defined timestamp (date and time).
  - The message content in a styled bubble.

## 🚀 How to Run
1. Make sure you have Python installed (version 3.x).
2. Run the script using:

   ```bash
   python main.py
   ```
   Enter the names of the two participants when prompted.
3. Click "Add Message" to input a new message, speaker, and timestamp.

## 🛠️ Requirements
1. Python 3.x
2. Tkinter (usually included with Python)

## 📝 Example Timestamp Format
When prompted for a timestamp, you can enter formats like:
2025-07-04 14:35
July 4, 2025 2:35 PM

## 📦 File Structure
main.py   # Main application script
README.md                # Project documentation

## 📄 License
This project is open-source and free to use under the MIT License.
