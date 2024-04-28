import google.generativeai as genai

placeholder = not bool(input('> run live?'))
print('placeholder: ' + str(placeholder))

genai.configure(api_key="YOUR_API_KEY") # YOUR_API_KEY should be replaced with the API key you received from Google

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

sysprompt = "Hello! I am a bot. I am here to help you."

convo.send_message(sysprompt)

def bot_reply(sender, text):
    s = ''
    if not placeholder:
        sender_and_text = sender + ': ' + text
        try:
          convo.send_message(sender_and_text)
          s = convo.last.text
        except:
          s = "Woah woah, slow down buddy."
    else:
        s = 'I am not available right now. Please try again later.'
    return s

