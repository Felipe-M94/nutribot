import pytest
from unittest.mock import patch
from nutribot.bot import NutriBot


@patch("builtins.input", side_effect=["25", "70", "175", "manutenção"])
def test_collect_user_data(mock_input):
    """Testa a coleta de dados do usuário."""
    bot = NutriBot()
    bot.collect_user_data()

    expected_data = {
        "idade": 25,
        "peso": 70.0,
        "altura": 175.0,
        "objetivo": "manutenção",
    }
    assert (
        bot.user_data == expected_data
    ), f"Esperado: {expected_data}, mas recebeu: {bot.user_data}"


@patch("builtins.input", side_effect=["25", "70", "175", "ganho de massa muscular"])
def test_calculate_daily_calories(mock_input):
    """Testa o cálculo de calorias diárias."""
    bot = NutriBot()
    bot.collect_user_data()
    bot.calculate_daily_calories()

    # Calculando as calorias esperadas
    base_calories = 1.2 * (10 * 70 + 6.25 * 175 - 5 * 25 + 5) + 500
    assert (
        bot.daily_calories == base_calories
    ), f"Esperado: {base_calories}, mas recebeu: {bot.daily_calories}"


@patch("builtins.input", side_effect=["registrar refeição", "sair"])
def test_interact(mock_input):
    """Testa o método de interação principal do bot."""
    bot = NutriBot()

    with patch.object(bot, "collect_user_data") as mock_collect_data, patch.object(
        bot, "log_meal"
    ) as mock_log_meal:

        mock_collect_data.return_value = None
        mock_log_meal.return_value = None

        bot.interact()

        # Garantir que os métodos principais foram chamados
        mock_collect_data.assert_called_once()
        mock_log_meal.assert_called_once()
