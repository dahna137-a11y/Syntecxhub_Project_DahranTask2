
import datetime

knowledge_base = {
    "what is python": "Python is a programming language.",
    "what is ai": "AI stands for Artificial Intelligence.",
    "what is chatbot": "A chatbot is a program that talks to users."
}

def get_response(user_input):
    user_input = user_input.lower()
    if user_input in ["hi", "hello", "hey"]:
        return "Hello! How can I help you?"
    elif "help" in user_input:
        return "You can ask me about Python, AI, and chatbots."
    elif "how are you" in user_input:
        return "I am fine 😊. How about you?"
    elif user_input in knowledge_base:
        return knowledge_base[user_input]
    elif user_input == "bye":
        return "Goodbye!"
    else:
        return "Sorry, I don't understand."

print("Chatbot started! Type 'bye' to exit.")

while True:
    user = input("You: ")
    if user.lower() == "bye":
        print("Bot: Goodbye!")
        break
    response = get_response(user)
    print("Bot:", response)
    with open("chat_log.txt", "a") as file:
        time = datetime.datetime.now()
        file.write(f"{time} You: {user}
")
        file.write(f"{time} Bot: {response}
")
