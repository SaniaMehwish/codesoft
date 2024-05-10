import random

# Define rules for the chatbot
rules = {
    "hi": ["Hello!", "Hi there!", "Hey!"],
    "how are you?": ["I'm doing well, thank you!", "I'm fine, thanks for asking."],
    "what's your name?": ["I'm a chatbot.", "You can call me chatbot."],
    "bye": ["Goodbye!", "See you later!", "Bye!"]
}

def chatbot_response(user_input):
    user_input = user_input.lower()
    for key in rules:
        if user_input == key:
            return random.choice(rules[key])
    return "I'm sorry, I don't understand that."

# Main function to interact with the chatbot
def main():
    print("Chatbot: Hello! How can I assist you today?")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'bye':
            print("Chatbot:", chatbot_response(user_input))
            break
        print("Chatbot:", chatbot_response(user_input))

if __name__ == "__main__":
    main()
