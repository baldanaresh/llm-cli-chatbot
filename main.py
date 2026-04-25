import os
from google import genai
from dotenv import load_dotenv

def main(): 
    load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY")
    
    if not api_key:
        print("Error: GEMINI_API_KEY not found.")
        return

    client = genai.Client(api_key=api_key)
    
    model_id = "gemini-2.5-flash"
    
    # Define your persona
    persona = "You are straight forward no suger coated chatbot that answers questions in a concise manner. You do not provide any additional information or context beyond what is asked. You do not engage in small talk or provide opinions. Your responses are direct and to the point."

    print(f"--- Gemini Chatbot Started ---")

    # FIX: Pass system_instruction directly as an argument to the chat creator
    # Some SDK versions prefer it here to avoid the JSON 'field not found' error
    chat = client.chats.create(
        model=model_id,
        config={
            'system_instruction': persona,
            'temperature': 0.7
        }
    )

    while True:
        try:
            user_input = input("You: ").strip()
            if user_input.lower() in ["exit", "quit"]:
                break
            
            if not user_input:
                continue

            response = chat.send_message(user_input)
            print(f"Bot: {response.text}\n")

        except Exception as e:
            # If the error persists, it's often a naming convention issue (system_instruction vs systemInstruction)
            print(f"An error occurred: {e}")
            break

if __name__ == "__main__":
    main()