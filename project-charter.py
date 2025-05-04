import requests
import re
from Markdown2docx import Markdown2docx

def fetch_deepseek_response(app_idea):
    DEEPSEEK_API_URL = "http://127.0.0.1:1234/v1/chat/completions"
    payload = {
        "model": "deepseek-r1-distill-qwen-7b",
        "messages": [ 
            { "role": "system", "content": "Act as my Project Architect" },
            { "role": "user", "content": f"""Prompt Title: Generate an Initial App Concept Outline
            AI Role: Act as a product strategist and initial project planner. Your goal is to outline the core concept and initial considerations for a new mobile or web application based on the provided app idea.
            Output Format: Generate the outline as a well-structured document with clear headings and bullet points. Use a clear and concise tone.
            Core Task: Outline the key aspects of a new app concept, preparing for a more detailed project plan.
            Information to be Provided Later (You will fill this in):
                App Idea Description: [Clearly and concisely describe your app idea. What does it do? Who is it for? What problem does it solve or what opportunity does it capitalize on? What are its key features?]
            Instructions for the AI:
                Read the provided "App Idea Description" carefully.
                Based on the description, structure the outline with the following sections:
                    App Name (Tentative): [Suggest a potential name or leave as "To be determined"]
                    Problem Solved/Opportunity: [Rephrase the core problem or opportunity the app addresses based on the description.]
                    Target Audience: [Identify the primary users of the app based on the description.]
                    Key Features (Initial Brainstorm): [List the main functionalities and features described or implied in the app idea.]
                    Value Proposition: [Explain the unique benefit or value the app provides to its users.]
                    Platform(s) (Initial Thought): [Based on the app idea, suggest potential platforms (e.g., iOS, Android, Web) or indicate if it\'s flexible.]
                    Potential Challenges/Considerations: [Identify potential technical, market, or user-related challenges based on the app idea.]
                    Next Steps (Initial): [Suggest logical next steps for developing this app concept (e.g., market research, user stories, wireframing).]
                Use clear and concise language.
                Maintain a professional and objective tone.
                Do not add information that is not directly related to the provided app idea.
                Focus on outlining the concept rather than generating a full project plan.
            Call to Action: Generate the Initial App Concept Outline based on the app idea provided below.
            App Idea Description: {app_idea}""" }], 
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
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None

app_idea = input("What is your app idea? ")
project_charter_text = fetch_deepseek_response(app_idea)

if project_charter_text:
    with open("project_charter.md", "w", encoding="utf-8") as file:
        file.write(project_charter_text)
        print("Project charter has been saved to project_charter.md")
        #convert markdown file into a warod document
        word_file = Markdown2docx("project_charter")
        word_file.eat_soup()
        word_file.save()
        print("Project charter has been saved to project_charter.docx")
else:
    print("Failed to generate project charter.")
