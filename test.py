import requests


# Step 1 Find API URL
DEEPSEEK_API_URL = "http://127.0.0.1:1234/v1/chat/completions"

# Step 2 Build request 
payload = {
    "model": "deepseek-r1-distill-qwen-7b",
    "messages": [ 
      { "role": "system", "content": "Always answer in rhymes." },
      { "role": "user", "content": "Introduce yourself." }
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
    generated_text = response_json['choices'][0]['message']['content'] #gives only the generated text
    #without everything behind response_json -> all Metadata with id object created model ....
    print("Generated Text:", generated_text)