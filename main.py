import os
from google import genai
from dotenv import load_dotenv

def main(): 
    # Load environment variables from a .env file into the system's environment
    load_dotenv()
    
    # Retrieve the API key from the environment variables
    api_key = os.getenv("GEMINI_API_KEY")
    
    # Check if the API key exists; if not, alert the user and stop execution
    if not api_key:
        print("Error: GEMINI_API_KEY not found.")
        return

    # Initialize the GenAI client with your API key and set the API version to stable v1
    client = genai.Client(
        api_key=api_key,
        http_options={'api_version': 'v1'}
    )
    
    # Specify the model identifier for the current 2.5-flash workhorse model
    model_id = "gemini-2.5-flash"

    print(f"Gemini Chatbot started using {model_id}! Type 'exit' to quit.\n")

    # Create a persistent chat session to maintain conversation context (memory)
    chat = client.chats.create(model=model_id)

    # Start an infinite loop to handle the interactive conversation
    while True:
        # Get input from the user and strip leading/trailing whitespace
        user_input = input("You: ").strip()

        # Exit the loop and end the program if the user types 'exit'
        if user_input.lower() == "exit":
            print("Chat ended.")
            break

        # If the input is empty (e.g., just pressing Enter), restart the loop
        if not user_input:
            continue

        try:
            # Send the user's message to the chat session and get the model's response
            response = chat.send_message(user_input)
            
            # Print the text content returned by the AI
            print(f"Bot: {response.text}\n")

        except Exception as e:
            # Catch and display any errors (e.g., network issues or invalid model IDs)
            print(f"Error: {e}")

# Ensure the main function runs only if this script is executed directly
if __name__ == "__main__":
    main()