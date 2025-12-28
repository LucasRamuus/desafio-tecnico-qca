import pdfplumber
import re
from datetime import datetime
from models import Invoice, Item


class PDFIngestor:
    """
    Responsável por realizar a ingestão de dados a partir de arquivos PDF,
    extraindo as informações da fatura e convertendo para o modelo Invoice.
    """

    def extract_invoice(self, pdf_path: str) -> Invoice:
        with pdfplumber.open(pdf_path) as pdf:
            # Extrai todo o texto do PDF para buscar os metadados da fatura
            text = "\n".join(page.extract_text() for page in pdf.pages)

            items = []

            # Percorre todas as páginas em busca da tabela de itens
            for page in pdf.pages:
                table = page.extract_table()
                if not table:
                    continue

                # Ignora o cabeçalho da tabela (primeira linha)
                for row in table[1:]:
                    if not row or len(row) < 4:
                        continue

                    # A primeira coluna (Product ID) não é necessária no desafio
                    _, product, quantity, unit_price = row

                    # Garante que os dados essenciais existam
                    if not product or not quantity or not unit_price:
                        continue

                    # Cria o item validado pelo Pydantic
                    items.append(
                        Item(
                            product=product.strip(),
                            quantity=int(quantity),
                            unit_price=float(unit_price)
                        )
                    )

        # Extração dos metadados da fatura via regex
        order_id = re.search(r"Order ID:\s*(\S+)", text).group(1)
        date_str = re.search(r"Date:\s*(\d{4}-\d{2}-\d{2})", text).group(1)
        customer_id = re.search(r"Customer ID:\s*(\S+)", text).group(1)

        # Retorna a fatura já validada
        return Invoice(
            order_id=order_id,
            date=datetime.strptime(date_str, "%Y-%m-%d").date(),
            customer_id=customer_id,
            items=items
        )
