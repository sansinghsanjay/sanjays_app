# python imports
import requests

# constants
FASTAPI_URL = "http://localhost:8000"
ROOT_ENDPOINT = "/"

# calling root endpoint
response = requests.post(
    FASTAPI_URL + ROOT_ENDPOINT
)
response = response.json()
print("Root Endpoint: " + response["response"])