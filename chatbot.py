# Todo: Develop Funktional Chatbot
# - ENgages in Realtime Conversation
# - Maintains Context

import requests
import re


def DeepseekChatbot():
    messages = [
            { "role": "system", "content": "Act as a friendly Chatbot" }     
    ]
    while True:
        DEEPSEEK_API_URL = "http://127.0.0.1:1234/v1/chat/completions"
        input_message = input("You: ")
        if input_message.lower() == "exit":
            print("Exiting the chatbot. Goodbye!")
            break
        messages.append({ "role": "user", "content": input_message})
        payload = {
            "model": "deepseek-r1-distill-qwen-7b",
            "messages": messages,
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
            print("Chatbot:", filtered_answer)


DeepseekChatbot()
