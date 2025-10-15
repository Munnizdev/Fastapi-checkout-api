# Microsserviço de Regras de Preço (Pricing Engine)

## Sumário
Microsserviço RESTful construído em **Python** com **FastAPI**. Implementa a lógica central de um *Pricing Engine* para processamento de checkout e aplicação de descontos complexos (e.g., BOGO).

## Arquitetura e Padrões de Engenharia

O projeto demonstra rigor em padrões de arquitetura e código:

* **Arquitetura:** Aplica o princípio de **Separação de Responsabilidades** (SoC) com **Clean Architecture** (Interface/Controller em `main.py` e Lógica de Negócio em `promotion_service.py`).
* **OOP/SOLID:** Demonstra o **Princípio Aberto/Fechado (OCP)** através de classes abstratas e herança na lógica de desconto.
* **Observabilidade:** Utiliza `logging` estruturado para rastreamento de requisições, simulando integração com ferramentas como Datadog ou Kibana.
* **Segurança:** Implementa boas práticas de **12-Factor App** ao segregar configurações (`SECRET_KEY`, `LOG_LEVEL`) do código-fonte via **`.env`** e `python-dotenv`.

## Setup Rápido

O serviço é configurado via `requirements.txt` e pode ser executado facilmente:

```bash
# Clone e navegue
git clone [https://github.com/Munnizdev/Fastapi-checkout-api.git](https://github.com/Munnizdev/Fastapi-checkout-api.git)
cd Fastapi-checkout-api

# Setup e execução
pip install -r requirements.txt
# Criar arquivo .env
uvicorn main:app --reload
