# Learning / Info

For learning and doing my first steps with AI Agents

## intro

import Request and get your Server Address from the top right of the LM Studio.
per default.
http://127.0.0.1:1234

Check Documentation and get Check on how to build a Request.

Payload = {
    "model": "deepseek-r1-distill-qwen-7b",
    "messages": [ 
      { "role": "system", "content": "Always answer in rhymes." },
      { "role": "user", "content": "Introduce yourself." }
    ], 
    "temperature": 0.7, # Between 0.0 - 2.0 .0 - .3 very Direct and correct, 0.7 - 2.0 more Creative
    "max_tokens": -1, #limit of tokens for answer (1 toke = 4 Chars in english letter) -1 = infinite
    "stream": true
  }

Fetch response 
response = requests.post(DEEPSEEK_API_URL,json=payload)

Parse the response 

generated_text = response_json['choices'][0]['message']['content'] 
This will only give the Response Text without the Metadata like id object model ....

But better use get
.get() will return None without raising an exception, allowing your program to handle the situation rather than crashing.


## healt-data
How to deal with Files in Python. 

