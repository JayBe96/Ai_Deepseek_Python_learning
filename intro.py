import requests
import re


# Step 1 Find API URL
DEEPSEEK_API_URL = "http://127.0.0.1:1234/v1/chat/completions"

user_prompt = input("Enter your prompt: \n")
# Step 2 Build request 
payload = {
    "model": "deepseek-r1-distill-qwen-7b",
    "messages": [ 
      { "role": "system", "content": "Act as if you where a expert like Mark Rober, Huberman or Tim Ferriss" },
      { "role": "user", "content": user_prompt }
    ], 
    "temperature": 0.7, 
    "max_tokens": -1,
    "stream": False,
  }

# Step 3 invoke the API + fetch response
response = requests.post(
    DEEPSEEK_API_URL,
    json=payload)

# Step 4 Parse API response

if response.status_code == 200:
    response_json = response.json()
    answer = response_json.get('choices')[0].get('message').get('content')
    filtered_answer = re.sub(r"<think>.*</think>","",answer,flags=re.DOTALL).strip()
    # print("Generated Antwort:", answer)
    print("Generated gefilterte Antwort:", filtered_answer)