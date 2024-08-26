from dotenv import load_dotenv
import os

# load environment variables from .env file
load_dotenv()

# get the environment variable
api_key=os.environ.get("OPENAI_API_KEY")
print(api_key)