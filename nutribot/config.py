import os
from dotenv import load_dotenv

load_dotenv()

FOOD_FACTS_API_URL = os.getenv("FOOD_FACTS_API_URL")
SPOONACULAR_API_KEY = os.getenv("SPOONACULAR_API_KEY")
