import load_dotenv
import os
import google.generativeai as genai

# Load environment variables from .env file
load_dotenv.load_dotenv()
# Access the environment variable
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
print(f"Google API Key: {GOOGLE_API_KEY}")

# Configure the generative AI client
genai.configure(api_key=GOOGLE_API_KEY)

# Create the model
model = genai.GenerativeModel('gemini-pro')

def make_llm_call(prompt):
    """Make a basic LLM call to the Google Generative AI model."""
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error making LLM call: {str(e)}"

# Example usage
if __name__ == "__main__":
    test_prompt = "Hello! Can you tell me what you are?"
    result = make_llm_call(test_prompt)
    print(f"LLM Response: {result}")