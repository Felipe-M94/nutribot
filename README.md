# NutriBot Documentation

## **Visão Geral do Projeto**

O **NutriBot** é um chatbot projetado para ajudar os usuários a planejar suas refeições, registrar sua ingestão calórica e obter feedback personalizado com base em seus objetivos nutricionais. O projeto foi desenvolvido com foco em fornecer uma solução interativa, acessível e educativa para gestão de dietas.

---

## **Tecnologias Utilizadas**

O projeto utiliza as seguintes tecnologias:

- **Python**: Linguagem principal para o desenvolvimento do bot.
- **SpaCy**: Biblioteca para processamento de linguagem natural (NLP), usada para interpretar descrições das refeições dos usuários.
- **Requests**: Biblioteca para requisições HTTP, utilizada para buscar informações nutricionais em APIs externas.
- **Python-dotenv**: Biblioteca para carregamento de variáveis de ambiente a partir de um arquivo `.env`.
- **Poetry**: Gerenciador de dependências e ferramentas de empacotamento.
- **Taskipy**: Plugin para organizar e executar scripts predefinidos como tarefas no projeto.
- **pytest**: Framework para testes automatizados, garantindo a funcionalidade e qualidade do código.
- **Ruff**: Ferramenta para linting e formatação do código Python.
- **Coverage.py**: Utilizado para medir a cobertura de testes.

---

## **Estrutura do Projeto**

A estrutura básica do projeto é:

```
project_root/
├── nutribot/
│   ├── __init__.py
│   ├── bot.py
│   ├── utils.py
│   ├── config.py
├── tests/
│   ├── __init__.py
│   ├── test_bot.py
│   ├── test_utils.py
├── .env
├── .gitignore
├── pyproject.toml
├── README.md
```

- **nutribot/**: Diretório principal contendo os arquivos do chatbot.
  - **bot.py**: Contém a classe `NutriBot` e a lógica principal do chatbot.
  - **utils.py**: Contém funções auxiliares para processamento de entrada e busca de informações nutricionais.
  - **config.py**: Carrega configurações sensíveis a partir do arquivo `.env`.
- **tests/**: Diretório com testes automatizados para validar as funcionalidades do projeto.
- **.env**: Arquivo para armazenar credenciais e configurações sensíveis.
- **.gitignore**: Arquivo para ignorar arquivos desnecessários no repositório Git.
- **pyproject.toml**: Arquivo de configuração do Poetry, Taskipy e dependências.
- **README.md**: Documentação do projeto.

---

## **Configuração e Instalação**

### **Variáveis de Ambiente**
Crie um arquivo `.env` na raiz do projeto e adicione as seguintes variáveis:

```
FOOD_FACTS_API_URL=<URL_DA_API_DE_NUTRIÇÃO>
SPOONACULAR_API_KEY=<SUA_CHAVE_DA_API_SPOONACULAR>
```

### **Pré-requisitos**

1. Certifique-se de ter o Python 3.11 ou superior instalado.
2. Instale o Poetry:
   ```bash
   pip install poetry
   ```

### **Passo a Passo**

1. **Clone o repositório**:
   ```bash
   git clone <URL_DO_REPOSITORIO>
   cd <DIRETORIO_CLONADO>
   ```

2. **Instale as dependências**:
   ```bash
   poetry install
   ```

3. **Ative o ambiente virtual do Poetry**:
   ```bash
   poetry shell
   ```

4. **Baixe o modelo SpaCy necessário**:
   ```bash
   python -m spacy download pt_core_news_sm
   ```

5. **Execute o chatbot**:
   ```bash
   poetry run python -m nutribot.bot
   ```

---

## **Utilizando o Projeto**

### **Execução do Chatbot**
Ao rodar o comando:
```bash
poetry run python -m nutribot.bot
```
O chatbot interagirá com você para:

1. Coletar dados pessoais (idade, peso, altura e objetivo).
2. Calcular a ingestão diária recomendada de calorias.
3. Fornecer um plano de refeições baseado no objetivo nutricional via API.
4. Registrar e analisar refeições consumidas.
5. Oferecer feedback com base no progresso calórico do usuário.

### **Executando Testes**
Para rodar os testes automatizados e verificar o funcionamento correto:
```bash
poetry run task test
```
Este comando:
- Executa os testes com `pytest`.
- Gera um relatório de cobertura de código com `coverage`.

### **Outras Tarefas Disponíveis**
As tarefas estão configuradas no `pyproject.toml`:

- **`task run`**: Executa o chatbot.
- **`task lint`**: Verifica a qualidade do código com `ruff`.
- **`task format`**: Corrige problemas de formatação no código.
- **`task test`**: Executa os testes automatizados.
- **`task pre_test`**: Linting antes de rodar os testes.
- **`task post_test`**: Gera um relatório HTML da cobertura de testes.

---

## **Contribuindo**

1. Crie um fork do repositório.
2. Crie uma branch para sua feature ou correção:
   ```bash
   git checkout -b minha-feature
   ```
3. Faça suas alterações e envie os commits.
4. Envie um Pull Request explicando suas alterações.

---

## **Contato**

Caso tenha dúvidas ou sugestões, entre em contato pelo e-mail **felipe.silva.mendonca@gmail.com**.

