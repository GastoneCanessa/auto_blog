# Automatic Blog with Django and OpenAI ChatGPT 📝

This project leverages Django to set up a blog that automatically generates a post after a specified period using OpenAI's ChatGPT.

## Requirements

- Python 3.6 or higher

## Installation & Setup


1. Clone the repository

git clone https://github.com/GastoneCanessa/auto_blog.git
cd auto_blog


2. Create a virtual environment

python3 -m venv env
source env/bin/activate  # On Windows, use `env\Scripts\activate`


3. Install dependencies

pip install -r requirements.txt

4. Setup .env file

OPENAI_KEY=your_openai_key
SECRET_KEY=your_secret_key_for_django

4. Run the project

#Start the asynchronous server with Daphne:
daphne project.asgi:application

# start the Redis server:
redis-server

# Start Celery Beat:
celery -A project beat --loglevel=info

# Start Celery Worker:
celery -A project worker --loglevel=info


# For any further assistance or issues, please [open a GitHub issue](https://github.com/GastoneCanessa/auto_blog/issues) or contact the repository owner.
