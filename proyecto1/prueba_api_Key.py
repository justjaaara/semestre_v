

import requests

# Replace with your OpenRouter API key
API_KEY = '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'
API_URL = 'https://openrouter.ai/api/v1/chat/completions'

# Define the headers for the API request
headers = {
    'Authorization': f'Bearer {API_KEY}',
    'Content-Type': 'application/json'
}

# Define the request payload (data)
data = {
    "model": "deepseek/deepseek-chat:free",
    "messages": [{"role": "user", "content": "Cómo puedo mejorar el consumo energético en mi hogar?"}]
}

# Send the POST request to the DeepSeek API
response = requests.post(API_URL, json=data, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    # print("API Response:", response.json())
    print("BBuscando....")
    content = response.json()["choices"][0]["message"]["content"]
    print("Extracted Content:", content)
else:
    print("Failed to fetch data from API. Status Code:", response.status_code)

