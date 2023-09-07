import openai
import os
from dotenv import load_dotenv


load_dotenv()

openai.api_key = os.environ.get("OPENAI_KEY")


def generate_post_content(prompt):
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=500
    )
    return response.choices[0].text.strip()