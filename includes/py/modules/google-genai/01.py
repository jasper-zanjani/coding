from google import genai
from dotenv import load_dotenv
from os import getenv

load_dotenv(dotenv_path='env')
api_key = getenv('GEMINI_API_KEY')

client = genai.Client(api_key=api_key)

response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents=["Greet me if you're there"]
)
print(response.text)
