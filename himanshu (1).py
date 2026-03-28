import random
import re

# ---------------- INTENTS ----------------
# You can expand this dictionary for more responses
intents = {
    "greeting": {
        "patterns": ["hello", "hi", "hey", "good morning", "good evening"],
        "responses": ["Hello! How can I help you today?", "Hi there! What can I do for you?", "Hey! Need assistance?"]
    },
    "product_query": {
        "patterns": ["price", "cost", "available", "product", "buy"],
        "responses": ["Our products range from $10 to $500 depending on your needs.", 
                      "We have multiple options. Can you specify the product?"]
    },
    "complaint": {
        "patterns": ["not working", "problem", "issue", "complain", "broken"],
        "responses": ["I am sorry to hear that. Can you describe the issue in detail?", 
                      "We apologize for the inconvenience. Let me assist you further."]
    },
    "goodbye": {
        "patterns": ["bye", "goodbye", "see you", "exit", "quit"],
        "responses": ["Goodbye! Have a great day!", "Bye! Let me know if you need more help.", "See you later!"]
    },
    "thanks": {
        "patterns": ["thanks", "thank you", "thx"],
        "responses": ["You're welcome!", "Happy to help!", "No problem!"]
    },
    "default": {
        "responses": ["I'm not sure I understand. Can you rephrase?", 
                      "Can you provide more details?", 
                      "Sorry, I didn't get that. Can you ask differently?"]
    }
}

# ---------------- FUNCTION: MATCH USER INPUT ----------------
def get_intent(user_input):
    user_input = user_input.lower()
    for intent, data in intents.items():
        for pattern in data.get("patterns", []):
            # simple keyword matching
            if re.search(r'\b' + re.escape(pattern) + r'\b', user_input):
                return intent
    return "default"

# ---------------- FUNCTION: GET RESPONSE ----------------
def get_response(intent):
    responses = intents.get(intent, intents["default"])["responses"]
    return random.choice(responses)

# ---------------- MAIN CHATBOT LOOP ----------------
def chatbot():
    print("🤖 Smart AI Customer Support Chatbot")
    print("Type 'exit' or 'bye' to end the chat.\n")

    while True:
        user_input = input("You: ").strip()
        if user_input == "":
            print("🤖 Please type something.")
            continue

        intent = get_intent(user_input)
        response = get_response(intent)

        print("🤖", response)

        if intent == "goodbye":
            break

# ---------------- RUN CHATBOT ----------------
if __name__ == "__main__":
    chatbot()