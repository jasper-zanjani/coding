from dotenv import dotenv_values, load_dotenv

load_dotenv()
api_key = dotenv_values('.env')['API_KEY']