# simulando um Microserviço
#OOP SOLID


class DiscountCalculator:
    """Classe base para calcular descontos."""
    def calculate_price(self, item_price: float, quantity: int) -> float:
        raise NotImplementedError("Subclasse deve implementar este método.")
    
class BogoDiscount(DiscountCalculator):
    """Implementa a regra Buy One Get One (Pague 1, Leve 2 - o mais caro é grátis)"""

    def calculate_price(self, item_price: float, quantity: int) -> float:
        """Calcula o preço total com a promoção BOGO."""
        if quantity <= 0 or item_price <= 0:
            return 0.0
        
        paid_items = quantity - (quantity // 2)
        total_price = paid_items * item_price

        return round(total_price, 2)