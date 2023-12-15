import google.generativeai as genai
from PIL import Image
import env

# Configure the model
genai.configure(api_key=env.key)
model = genai.GenerativeModel(model_name='models/gemini-pro')
image_model = genai.GenerativeModel(model_name='models/gemini-pro-vision')

# Generate single content from the AI
"""
response = model.generate_content('how many objects are in the solar system?')
print(response.text)
"""

# Have a conversation with the AI
"""
chat = model.start_chat()
while True:
    prompt = input('>>> ')
    response = chat.send_message(prompt.strip())
    print('Gemini:\n', response.text)
"""

# Using images
"""
result = image_model.generate_content(
    ['What do you think about this image?', Image.open('path to the image')]
)
print(result.text)
"""
