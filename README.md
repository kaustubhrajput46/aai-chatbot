# AAI Hands-On Assignment 3 — Create a Simple Q&A Chatbot with Python

## Description
This is a terminal-based Q&A chatbot built using Python. Due to known compatibility issues with ChatterBot in Python 3.10+, this implementation uses a custom pattern-matching and rule-based approach using Python's standard library (`re` module). It includes a knowledge base of over 15 Q&A pairs, responds to greetings, and logs conversations to `chat_log.txt`.

## Prerequisites
- Python 3.x

## How to Run
1. Open a terminal and navigate to the directory containing the code.
2. Run the chatbot script:
   ```bash
   python chatbot.py
   ```
3. Type your messages at the `user:` prompt.
4. Type `exit`, `quit`, or `bye` to end the conversation.

## Features
- **Greetings:** Responds to standard greetings like "hello", "hi", etc.
- **Q&A Knowledge Base:** Answers questions about Python, the weather, the current time, its creator, the instructor, and more.
- **Conversation Logging:** Saves all interactions to `chat_log.txt`.
- **Exit Command:** Gracefully exits the application when requested.
