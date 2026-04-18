from dotenv import load_dotenv
import os
import google.generativeai as genai

# Load environment variables from .env file
load_dotenv()
# Access the environment variable
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
if not GOOGLE_API_KEY:
    raise ValueError("GOOGLE_API_KEY environment variable is not set. Please configure it in your .env file.")

# Configure the generative AI client
genai.configure(api_key=GOOGLE_API_KEY)

# List available models and select one
def get_available_models():
    """Get list of available models from the API."""
    try:
        models = genai.list_models()
        available_models = []
        for model in models:
            if 'generateContent' in model.supported_generation_methods:
                available_models.append(model.name)
        return available_models
    except Exception as e:
        print(f"Error listing models: {e}")
        return []

# Get first available model
available_models = get_available_models()
if available_models:
    model_name = available_models[0].replace('models/', '')
    print(f"Available models: {[m.replace('models/', '') for m in available_models[:5]]}")
    print(f"Using model: {model_name}")
else:
    print("Warning: Could not fetch available models. Using default 'gemini-pro'")
    model_name = 'gemini-pro'

# Create the model
model = genai.GenerativeModel(model_name)


def make_llm_call(prompt: str) -> str:
    """
    Make an LLM call to the Google Generative AI model.
    
    Args:
        prompt (str): The prompt to send to the LLM
        
    Returns:
        str: The generated response from the LLM
        
    Raises:
        Exception: If the API call fails
    """
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        error_msg = f"Error making LLM call: {str(e)}"
        print(error_msg)
        raise


# Example usage and testing
if __name__ == "__main__":
    print("=" * 50)
    print("Testing LLM Client")
    print("=" * 50)
    
    # Test 1: Basic greeting
    print("\n[Test 1] Basic greeting")
    try:
        result = make_llm_call("Hello! Can you tell me what you are?")
        print(f"✓ Success\nResponse: {result}\n")
    except Exception as e:
        print(f"✗ Failed: {e}\n")
    
    # Test 2: Math question
    print("[Test 2] Math question")
    try:
        result = make_llm_call("What is 2 + 2?")
        print(f"✓ Success\nResponse: {result}\n")
    except Exception as e:
        print(f"✗ Failed: {e}\n")
    
    # Test 3: Creative writing
    print("[Test 3] Creative writing")
    try:
        result = make_llm_call("Write a short haiku about programming.")
        print(f"✓ Success\nResponse: {result}\n")
    except Exception as e:
        print(f"✗ Failed: {e}\n")
    
    print("=" * 50)
    print("Testing complete!")
    print("=" * 50)