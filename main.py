import logging
from typing import Dict
from fastapi import FastAPI, HTTPException
from promotion_service import BogoDiscount

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

app = FastAPI(title="Checkout API - Microsserviço de Regras de preço")

bogo_calc = BogoDiscount()

@app.post("/checkout")
async def process_checkout(data: Dict):
    """
    Endpoint que calcula o preço total após aplicar a regra BOGO.
    A entrada simula um JSON vindo de um front-end ou outro microsserviço.
    """
    try:
        item = data.get("item")
        price = data.get("price")
        quantity = data.get("quantity")

        if not all([item, price, quantity]):
           logging.warning("400 - Requisição inválida: Campos faltando.")
           raise HTTPException(status_code=400, detail="Item, price e quantity são obrigatórios.")

        logging.info("Cálculo concluído: Preço final={final_price}")

        return {
    "item": item,
    "quantity": quantity,
    "final_price": final_price,
    "discount_applied": "BOGO"
    }

    except Exception as e:
        logging.error(f"Erro inesperado no checkout: {e}", exc_info=True)
    raise HTTPException(status_code=500, detail="Erro interno ao processar o checkout.")

