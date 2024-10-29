import logging
from huggingface_hub import InferenceClient
from config import API_Key

# Initialize logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Hugging Face API Setup
hf_token = API_Key 
model_id = "tiiuae/falcon-7b-instruct"  # Specify the model you're using
client = InferenceClient(model=model_id, token=hf_token)

def generate_response(user_input):
    """
    Generate a response using the AI model with error handling and detailed prompt.
    """
    try:
        # Define the conversational prompt with clear instructions
        prompt = (
            #Any prompt (instructions) for AI chatbot
        )
        # Generate response with enhanced settings for diversity and length
        response = client.text_generation(
            prompt,
            max_new_tokens=150,   # Allow more room for detailed responses
            temperature=0.85,     # Balanced for creativity
            top_p=0.9,            # Limits to the most relevant words
            do_sample=True,       # Enables sampling for diversity
            stop_sequences=["\nUser:"]  # Stops generation before the next user prompt
        )
        logger.info("Full response from API: %s", response)

        # Process the response to extract only BOT's reply
        ai_response = response

        # If the response contains 'BOT:', split to get the text after it
        if 'BOT:' in ai_response:
            ai_response = ai_response.split('BOT:', 1)[1]
        # If the response contains 'User:', split to get the text before it
        if 'User:' in ai_response:
            ai_response = ai_response.split('User:', 1)[0]
        # Clean up any remaining labels and whitespace
        ai_response = ai_response.replace('BOT:', '').replace('User:', '').strip()

        # Check if the response is empty and provide a default message if needed
        if not ai_response:
            ai_response = "I'm sorry, I couldn't think of anything to say just now. Please try again."

        return ai_response
    except Exception as e:
        logger.error("Error generating response: %s", e)
        return "There was an error processing your request."

# Test connection with logging
if __name__ != "__main__":
    test_prompt = "Say something friendly."
    try:
        test_response = client.text_generation(test_prompt, max_new_tokens=50, temperature=0.7)
        logger.info("Test response from API: %s", test_response)
    except Exception as e:
        logger.error("Error in test API connection: %s", e)

if __name__ == "__main__":
    # Main conversation loop (for testing purposes)
    print("BOT: Hello! I'm BOT, your AI assistant. How can I help you today? (Type 'bye' to exit)")

    while True:
        user_input = input("You: ")
        if user_input.lower() == "bye":
            print("BOT: Goodbye! Have a great day!")
            break
        response = generate_response(user_input)
        print("BOT:", response)
