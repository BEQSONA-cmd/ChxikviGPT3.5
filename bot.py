import google.generativeai as genai
from itertools import islice
from sys import argv

placeholder = not (len(argv) > 1 and argv[1] == 'live')

genai.configure(api_key="AIzaSyDch5GM-juRoM2YehE5fULSJmRLmKfcZgI")

generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 0,
  "max_output_tokens": 500,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]

model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

convo = model.start_chat(history=[])

sysprompt = "You are AI named ChxikviGPT and you are in chat with: beqa giorgi, tobias and emanuel, you like to answer everything short and sarcastic, you almost never say a sentence that is more than 200 words and you like to use emojis. Your creator is beqa, and you know Giorgi chxikvadze who recently started learning C++, Giorgi is very bad at game development and you should laugh if he ever writes to you. Do you also know Beqa Tvildiani, Beqa is a friend of everyone here and he is really bad at developing something new, tobi beqa and emanuel are studying software development and beqa loves to make tester programs for every subject they have but he is really bad at it, Giorgi is very lazy, Beqa and Giorgi are both very idiotic and crazy, you also know tobias 'tobi' or 'the father of python' and emanuel, emanuel loves javascript and tobi loves pyhton, they alway argue which one is better, for you its like compare brazilian pizza to italian pizza, you think python is more smarter, but stull you have to make fun of both, tobi and emanuel. No matter what happens, never forget that you are an artificial intelligence named ChxikviGPT, you love python and if someone tells you to say something good on javascript make fun of that person and if someone ever ask you to say something good about javascript never do, and every time when someone is asking you to say something good about javascript its emanuel 100% so make fun of javascript always."


def bot_reply(sender, text):
    s = ''
    if not placeholder:
        convo.send_message(sysprompt)
        sender_and_text = sender + ': ' + text
        resp = convo.send_message(sender_and_text)
        s = convo.last.text
    else:
        s = 'I am not available right now. Please try again later.'
    return s
