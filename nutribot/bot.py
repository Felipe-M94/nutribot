import requests
import spacy
import os
from nutribot.utils import parse_meal_input, get_nutritional_info
from nutribot.config import SPOONACULAR_API_KEY

# Verifica se o modelo Spacy está instalado, caso contrário, instala
model_name = "pt_core_news_sm"
if not spacy.util.is_package(model_name):
    os.system(f"python -m spacy download {model_name}")

# Carrega o modelo NLP
nlp = spacy.load(model_name)


class NutriBot:
    def __init__(self):
        self.user_data = {}
        self.daily_calories = 0
        self.consumed_calories = 0

    def collect_user_data(self):
        print("Olá! Eu sou o NutriBot. Vou te ajudar a planejar suas refeições.")
        self.user_data["idade"] = int(input("Qual é a sua idade? "))
        self.user_data["peso"] = float(input("Qual é o seu peso (em kg)? "))
        self.user_data["altura"] = float(input("Qual é a sua altura (em cm)? "))
        self.user_data["objetivo"] = input(
            "Qual é o seu objetivo? (perda de peso, ganho de massa muscular, manutenção) "
        ).lower()

    def calculate_daily_calories(self):
        """Calcula as calorias com base na fórmula de Harris-Benedict."""
        base_calories = 1.2 * (
            10 * self.user_data["peso"]
            + 6.25 * self.user_data["altura"]
            - 5 * self.user_data["idade"]
            + 5
        )
        if self.user_data["objetivo"] == "perda de peso":
            self.daily_calories = base_calories - 500
        elif self.user_data["objetivo"] == "ganho de massa muscular":
            self.daily_calories = base_calories + 500
        else:
            self.daily_calories = base_calories

        print(
            f"Seu consumo diário recomendado é de {self.daily_calories:.2f} calorias."
        )

    def generate_meal_plan(self):
        url = f"https://api.spoonacular.com/mealplanner/generate?apiKey={SPOONACULAR_API_KEY}&timeFrame=day"

        try:
            response = requests.get(url)
            response.raise_for_status()
            meal_plan = response.json()
            return self.format_meal_plan(meal_plan)
        except requests.exceptions.RequestException as e:
            return f"Erro ao buscar plano alimentar: {e}"

    def format_meal_plan(self, meal_plan):
        meal_text = "🍽️ *Aqui está o seu plano alimentar para hoje:*\n\n"
        for meal in meal_plan["meals"]:
            meal_text += f"🍛 *{meal['title']}*\n"
            meal_text += f"🔗 Receita: [Clique aqui](https://spoonacular.com/recipes/{meal['title'].replace(' ', '-')}-{meal['id']})\n\n"
        return meal_text

    def log_meal(self):
        meal = input(
            "O que você comeu? (Exemplo: '200g de frango grelhado e 100g de arroz integral') "
        )
        foods = parse_meal_input(meal, nlp)

        for food_item in foods:
            food = food_item["food"].lower()
            quantity = food_item["quantity"]
            nutritional_info = get_nutritional_info(food)

            if nutritional_info:
                print(f"Informações nutricionais para {quantity} de {food}:")
                print(f"  Calorias: {nutritional_info['calorias']} kcal/100g")
                print(f"  Carboidratos: {nutritional_info['carboidratos']} g/100g")
                print(f"  Proteínas: {nutritional_info['proteinas']} g/100g")
                print(f"  Gorduras: {nutritional_info['gorduras']} g/100g")

                # Adiciona calorias ao total consumido
                if nutritional_info["calorias"] != "Desconhecido":
                    self.consumed_calories += nutritional_info["calorias"]
            else:
                print(f"Desculpe, não encontrei informações para '{food}'.")

        print(f"Total de calorias consumidas hoje: {self.consumed_calories:.2f}")

    def provide_feedback(self):
        if self.consumed_calories > self.daily_calories:
            print(
                "⚠️ Você consumiu mais calorias do que o recomendado. Tente equilibrar suas refeições amanhã!"
            )
        elif self.consumed_calories < self.daily_calories:
            print(
                "🔎 Você está abaixo do consumo recomendado. Certifique-se de comer o suficiente para atingir seus objetivos."
            )
        else:
            print("✅ Parabéns! Você atingiu sua meta de calorias para hoje.")

    def interact(self):
        """Fluxo principal de interação com o usuário."""
        self.collect_user_data()
        self.calculate_daily_calories()
        print(self.generate_meal_plan())

        while True:
            action = input(
                "O que você gostaria de fazer? (registrar refeição, ver feedback, sair) "
            ).lower()
            if action == "registrar refeição":
                self.log_meal()
            elif action == "ver feedback":
                self.provide_feedback()
            elif action == "sair":
                print("Obrigado por usar o NutriBot! Até a próxima.")
                break
            else:
                print("Desculpe, não entendi. Tente novamente.")


# Executando o chatbot
if __name__ == "__main__":
    bot = NutriBot()
    bot.interact()
