print("===================================")
print("       RULE-BASED AI CHATBOT")
print("===================================")
print("Hello! I am your chatbot.")
print("You can ask me simple questions.")
print("Type 'bye' to exit.\n")

while True:
    user_input = input("You: ").lower().strip()

    if user_input in ["hello", "hi", "hey"]:
        print("Bot: Hello! Nice to meet you!")

    elif "how are you" in user_input:
        print("Bot: I am doing great! Thank you for asking.")

    elif "your name" in user_input:
        print("Bot: My name is AI Chatbot.")

    elif "what can you do" in user_input:
        print("Bot: I can respond to simple questions using predefined rules.")

    elif "python" in user_input:
        print("Bot: Python is a popular programming language used in AI and Machine Learning.")

    elif "artificial intelligence" in user_input or user_input == "ai":
        print("Bot: Artificial Intelligence is the ability of machines to perform tasks that normally require human intelligence.")

    elif "thank you" in user_input or "thanks" in user_input:
        print("Bot: You're welcome!")

    elif user_input in ["bye", "exit", "quit"]:
        print("Bot: Goodbye! Have a nice day!")
        break

    else:
        print("Bot: Sorry, I don't understand that. Please try asking something else.")