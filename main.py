import os
import sys

from dotenv import load_dotenv
from google import genai
from google.genai import types

def main():
    load_dotenv()

    cmd_input = sys.argv

    if len(sys.argv) < 2:
        print("Error: No prompt provided.")
        sys.exit(1)

    user_prompt = sys.argv[1]
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    
    

    

    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]
    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages,
    )

    print(response.text)
    if "--verbose" in cmd_input:
        print(f"User prompt: {user_prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

    else:
        print(f"Response: {response.text}")

if __name__ == "__main__":
    main()