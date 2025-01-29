import requests
from nutribot.config import FOOD_FACTS_API_URL


def get_nutritional_info(food_name):
    # Busca informações nutricionais na API do Open Food Facts
    url = f"{FOOD_FACTS_API_URL}?search_terms={food_name}&search_simple=1&action=process&json=1"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data["products"]:
            # Pega o primeiro produto da lista
            product = data["products"][0]
            return {
                "calorias": product.get("nutriments", {}).get(
                    "energy-kcal_100g", "Desconhecido"
                ),
                "carboidratos": product.get("nutriments", {}).get(
                    "carbohydrates_100g", "Desconhecido"
                ),
                "proteinas": product.get("nutriments", {}).get(
                    "proteins_100g", "Desconhecido"
                ),
                "gorduras": product.get("nutriments", {}).get(
                    "fat_100g", "Desconhecido"
                ),
            }
    return None


def parse_meal_input(text, nlp):
    # Usa spaCy para extrair alimentos e quantidades
    doc = nlp(text)
    foods = []
    quantity = None
    for ent in doc.ents:
        if ent.label_ == "QUANTIDADE" or ent.label_ == "NUM":
            quantity = ent.text
        else:
            food = ent.text
            foods.append({"food": food, "quantity": quantity})
    return foods
