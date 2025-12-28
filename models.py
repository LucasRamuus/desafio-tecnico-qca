from pydantic import BaseModel, Field
from typing import List
from datetime import date


class Item(BaseModel):
    """
    Representa um item da fatura.
    Contém o nome do produto, a quantidade comprada
    e o preço unitário.
    """
    product: str
    quantity: int = Field(gt=0, description="Quantidade do produto (maior que zero)")
    unit_price: float = Field(gt=0, description="Preço unitário do produto (maior que zero)")


class Invoice(BaseModel):
    """
    Representa uma fatura (invoice), contendo os dados
    principais e a lista de itens comprados.
    """
    order_id: str
    date: date
    customer_id: str
    items: List[Item]

    @property
    def total_value(self) -> float:
        """
        Calcula o valor total da fatura somando:
        quantidade * preço unitário de cada item.
        """
        return sum(item.quantity * item.unit_price for item in self.items)
