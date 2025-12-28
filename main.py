from pathlib import Path
from pdf_ingestor import PDFIngestor
from repository import InvoiceRepository
from analytics import InvoiceAnalytics

# Pasta contendo os PDFs das faturas
PDF_FOLDER = Path("invoices/pdfs")

# Caminho do arquivo de armazenamento
DB_PATH = "database.json"


def main():
    """
    Executa o fluxo completo da aplicação:
    - Ingestão dos PDFs
    - Armazenamento das faturas
    - Execução das análises
    """

    # ---------- INGESTÃO ----------
    ingestor = PDFIngestor()
    repo = InvoiceRepository(DB_PATH)

    for pdf_file in PDF_FOLDER.glob("*.pdf"):
        invoice = ingestor.extract_invoice(pdf_file)
        repo.add_invoice(invoice)

    # ---------- ANALYTICS ----------
    analytics = InvoiceAnalytics(DB_PATH)

    print(f"Média do valor total das faturas: {analytics.average_invoice_value():.2f}\n")

    print(f"Produto com maior frequência de compra: {analytics.most_frequent_product()}\n")

    print("Valor total gasto por cada produto:")
    total_by_product = analytics.total_spent_by_product()
    for product, total in total_by_product.items():
        print(f" - {product}: {total:.2f}")
    print()

    print("Lista de produtos (Nome e Preço Unitário):")
    product_list = analytics.product_listing()
    for _, row in product_list.iterrows():
        print(f" - {row['product']}: {row['unit_price']:.2f}")


if __name__ == "__main__":
    main()
