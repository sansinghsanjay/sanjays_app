# python packages
import json
from dotenv import load_dotenv
import os
import requests

# paths
constants_path = os.path.abspath("./../constants.json")

# load constants.json
with open(constants_path, 'r', encoding='utf-8') as file:
    constants = json.load(file)

# load .env
dot_env_path = os.path.abspath("./../.env")
load_dotenv(dot_env_path)

# load perplexity API key
PERPLEXITY_API_KEY = os.getenv("PERPLEXITY_API_KEY")

# Set up the headers
headers = {
    "Authorization": f"Bearer {PERPLEXITY_API_KEY}",  # Replace with your actual API key
    "Content-Type": "application/json"
}

# Define the request payload
payload = {
    "model": constants["PERPLEXITY_MODEL"],
    "messages": [
        {
            "role": "user",
            "content": "Any major updates on Apple's share prices for tomorrow?"
        }
    ]
}

# Make the API call
response = requests.post(constants["PERPLEXITY_URL"], headers=headers, json=payload)

# Print the AI's response
response_json = response.json()
print("Citations: ", response_json["citations"])
print("\n\nResponse:")
print(response_json["choices"][0]['message']['content'])