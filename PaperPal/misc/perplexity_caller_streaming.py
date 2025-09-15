'''
IT IS NOT WORD BY WORD STREAMING SO NOT MUCH BENEFICIAL. OUTPUTS REPEATATIONS. 
RECOMMENDED: USE NON-STREAMING.
'''
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
    ],
    "stream": True
}

# Make the API call; streaming enabled
response = requests.post(constants["PERPLEXITY_URL"], headers=headers, json=payload)

# Process the streaming response (simplified example)
'''
IT IS NOT WORD BY WORD STREAMING SO NOT MUCH BENEFICIAL. OUTPUTS REPEATATIONS. 
RECOMMENDED: USE NON-STREAMING.
'''
for line in response.iter_lines():
    if line:
        line = line.decode("utf-8")
        json_line = json.loads(line[6:])
        #print("Citations: ", json_line["citations"])
        #print(json_line["choices"][0]["message"]["content"])
        print(json_line["usage"])
        print("")