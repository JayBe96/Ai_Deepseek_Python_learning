# AI Project Documentation

## Table of Contents
- [Project Overview](#project-overview)
- [Prerequisites](#prerequisites)
- [Installation Guide](#installation-guide)
- [Setting Up LM Studio](#setting-up-lm-studio)
- [Downloading DeepSeek b7 Qwen Distilled](#downloading-deepseek-b7-qwen-distilled)
- [Starting the Server in Developer Tag](#starting-the-server-in-developer-tag)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Project Overview
This project is designed to [brief description of what your project does]. 

## Prerequisites
- Python 3.13 


## Installation Guide
Follow these steps to set up the environment for your AI project.

### 1. Install Python
Make sure you have Python 3.13 installed. You can download it from the official website: [Python Download](https://www.python.org/downloads/).

### 2. Install LM Studio 
Visit the LM Studio official website and download the latest version [here](https://lmstudio.ai/download).

## Setting Up LM Studio


## install 
pip install requests

## Run

In this Retro there are some small things i wanted to try out. The diffrent Projects and how to run them. For all these LM Studio must run and the server needs to be actrive.

### intro
 Just lets you a send your Prompt to the LM Studio Local Deepseek API. 
```
python intro.py
```

### Medical advicer
 Intakes a csv file and gives advice on Health based on it
```
python health-data.py
```

### Chatbot
similar to the intro but here the context of the previous Chats are given. So you can have a conversation about a topic. with exit you end the programm
```
python chatbot.py
```

### Project
before running run install Markdown2docx. The Project will Create a markdown file and a wordfile which will indicate on how to do the Project.
```
pip install Markdown2docx
python .\project-charter.py
```
