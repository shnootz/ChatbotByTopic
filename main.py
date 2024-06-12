import random
from transformers import pipeline, Conversation

# Initialize the conversational pipeline
chatbot = pipeline(task="conversational", model="facebook/blenderbot-400M-distill")

# Define a list of random topics
random_topics = [
    "What is your favorite book and why?",
    "If you could travel anywhere in the world, where would you go?",
    "What's the most interesting fact you know?",
    "Tell me about a memorable experience you had recently.",
    "What are your thoughts on artificial intelligence?",
    "How do you like to spend your free time?",
    "What's your favorite food and why do you like it?",
    "What hobbies do you enjoy?",
    "Can you share a piece of advice you think is important?",
    "What's something new you learned recently?"
]

# Select a random topic to start the conversation
ai_initial_message = random.choice(random_topics)
print(f"AI: {ai_initial_message}")

# Initialize the conversation with the selected topic
conversation = Conversation(ai_initial_message)

# Function to interact with the AI
def chat_with_ai(conversation):
    while True:
        # User's response
        user_message = input("You: ")

        # Add user's response to the conversation
        conversation.add_user_input(user_message)

        # Get the AI's response
        conversation = chatbot(conversation)

        # Print the AI's response
        print(f"AI: {conversation.generated_responses[-1]}")

        # Check if the AI's response completes the conversation
        if conversation.generated_responses[-1] == ai_initial_message:
            break

# Start the interaction
chat_with_ai(conversation)
