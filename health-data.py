
import requests
import re


def fetch_deepseek_response(prompt):
    DEEPSEEK_API_URL = "http://127.0.0.1:1234/v1/chat/completions"
    payload = {
        "model": "deepseek-r1-distill-qwen-7b",
        "messages": [ 
        { "role": "system", "content": "Act as ia doctor" },
        { "role": "user", "content": prompt }
        ], 
        "temperature": 0.1, 
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
        return filtered_answer

CSV_FILE_PATH = "health.csv"

try:
    with open(CSV_FILE_PATH, "r") as file:
        cvs_data = file.readlines()
except FileNotFoundError:
    print(f"File {CSV_FILE_PATH} not found.")
    exit(1)

question = f"Analyze the data in {cvs_data} and provide a summary of the health data."
response = fetch_deepseek_response(question)

print(response)