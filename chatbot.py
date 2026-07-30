import json
import random
import re
import datetime
import os

class SimpleChatbot:
    def __init__(self, log_file="chat_log.txt"):
        self.log_file = log_file
        self.greetings = ["hello", "hi", "hey", "greetings", "good morning", "good afternoon", "good evening"]
        self.greeting_responses = [
            "Hello! How can I help you today?",
            "Hi there! What's on your mind?",
            "Greetings! I am ready to answer your questions."
        ]
        self.qa_knowledge_base = {
            r"how are you.*": "I am doing very well, thank you for asking.",
            r".*your name.*": "I am a simple Python chatbot created for a class assignment.",
            r".*created you.*": "I was created by a software engineering student.",
            r".*weather like.*": "I don't have access to real-time weather data, but I hope it's nice where you are!",
            r".*time is it.*": f"The current server time is {datetime.datetime.now().strftime('%H:%M:%S')}.",
            r".*meaning of life.*": "42, according to The Hitchhiker's Guide to the Galaxy.",
            r".*favorite color.*": "I like blue, like the ocean of data I process.",
            r".*tell me a joke.*": "Why do programmers prefer dark mode? Because light attracts bugs!",
            r".*python.*": "Python is a high-level, interpreted programming language known for its readability.",
            r".*capital of france.*": "The capital of France is Paris.",
            r".*how old are you.*": "I am as old as the code that runs me.",
            r".*artificial intelligence.*": "AI is the simulation of human intelligence processes by machines, especially computer systems.",
            r".*what can you do.*": "I can answer basic questions, greet you, and log our conversation.",
            r".*do you like hats.*": "I don't have a head, but hats seem quite practical for humans!",
            r".*thank you.*": "You're welcome! Do you have any other questions?",
            r".*who is the instructor.*": "The instructor for this course is Dr. V."
        }
        
    def log_interaction(self, user_input, bot_response):
        """Logs the conversation to a file."""
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(self.log_file, "a", encoding="utf-8") as f:
            f.write(f"[{timestamp}] User: {user_input}\n")
            f.write(f"[{timestamp}] Bot: {bot_response}\n\n")
            
    def get_response(self, user_input):
        """Generates a response based on pattern matching."""
        lower_input = user_input.lower().strip()
        
        # Check greetings
        if any(greet in lower_input for greet in self.greetings) and len(lower_input.split()) <= 3:
            return random.choice(self.greeting_responses)
            
        # Check QA Knowledge base
        for pattern, response in self.qa_knowledge_base.items():
            if re.search(pattern, lower_input):
                return response
                
        # Default response
        return "I'm not quite sure how to answer that. Could you try rephrasing?"

    def start_chat(self):
        print("Welcome to the Q&A Chatbot!")
        print("Type 'exit', 'quit', or 'bye' to end the conversation.")
        print("-" * 50)
        
        while True:
            try:
                user_input = input("user: ")
                if not user_input.strip():
                    continue
                    
                if user_input.lower() in ['exit', 'quit', 'bye']:
                    print("bot: Goodbye! Have a great day!")
                    self.log_interaction(user_input, "Goodbye! Have a great day!")
                    break
                    
                bot_response = self.get_response(user_input)
                print(f"bot: {bot_response}")
                self.log_interaction(user_input, bot_response)
                
            except KeyboardInterrupt:
                print("\nbot: Goodbye!")
                break
            except Exception as e:
                print(f"bot: Oops, an error occurred: {e}")
                break

if __name__ == "__main__":
    bot = SimpleChatbot()
    bot.start_chat()
