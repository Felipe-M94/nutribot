import pytest
from nutribot.utils import parse_meal_input, get_nutritional_info


@pytest.fixture
def nlp_model():
    """Carrega o modelo NLP usado no parse_meal_input."""
    import spacy

    return spacy.load("pt_core_news_sm")


def test_parse_meal_input(nlp_model):
    """Teste para verificar o parsing de refeições."""
    meal_input = "200g de frango grelhado e 100g de arroz integral"
    expected_output = [
        {"food": "frango grelhado", "quantity": 200},
        {"food": "arroz integral", "quantity": 100},
    ]

    result = parse_meal_input(meal_input, nlp_model)
    assert (
        result == expected_output
    ), f"Esperado: {expected_output}, mas recebeu: {result}"


def test_get_nutritional_info_success(mocker):
    """Teste para verificar a consulta de informações nutricionais com sucesso."""
    mock_response = {
        "calorias": 165,
        "carboidratos": 0,
        "proteinas": 31,
        "gorduras": 4,
    }

    # Mock da função requests.get para simular resposta da API
    mocker.patch(
        "requests.get",
        return_value=mocker.Mock(status_code=200, json=lambda: mock_response),
    )

    food = "frango grelhado"
    result = get_nutritional_info(food)

    assert result == mock_response, f"Esperado: {mock_response}, mas recebeu: {result}"


def test_get_nutritional_info_failure(mocker):
    """Teste para simular falha ao buscar informações nutricionais."""
    mocker.patch(
        "requests.get", return_value=mocker.Mock(status_code=404, json=lambda: {})
    )

    food = "alimento desconhecido"
    result = get_nutritional_info(food)

    assert (
        result is None
    ), "Deveria retornar None quando a API não encontra informações."
