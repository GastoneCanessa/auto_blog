import openai
import os
from dotenv import load_dotenv


load_dotenv()

openai.api_key = os.environ.get("OPENAI_KEY")


def generate_post_content(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", 
        messages=[
                {"role": "system", "content": "Sei un assistente che scrive post di alta qualità sulle innovazioni tecnologiche che hanno cambiato il mondo."},
                {"role": "user", "content": prompt}
            ]
    )
    return response.choices[0].message['content']