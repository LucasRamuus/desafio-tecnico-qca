import pandas as pd


class InvoiceAnalytics:
    """
    Responsável por realizar análises sobre as faturas armazenadas
    no arquivo database.json utilizando pandas.
    """

    def __init__(self, json_path: str = "database.json"):
        """
        Carrega o arquivo JSON contendo as faturas.

        :param json_path: Caminho do arquivo database.json
        """
        self.df = pd.read_json(json_path)

    def average_invoice_value(self) -> float:
        """
        Calcula a média do valor total das faturas.

        Para cada fatura:
        - Soma (quantidade * preço unitário) de seus itens
        - Calcula a média entre todas as faturas

        :return: Média do valor total das faturas
        """
        df = self.df.explode("items", ignore_index=True)

        items_df = pd.json_normalize(df["items"])
        items_df["order_id"] = df["order_id"]

        # Valor total por item
        items_df["total_item"] = items_df["quantity"] * items_df["unit_price"]

        # Soma por fatura
        invoice_totals = (
            items_df
            .groupby("order_id")["total_item"]
            .sum()
        )

        return invoice_totals.mean()

    def most_frequent_product(self) -> str:
        """
        Identifica o produto com maior frequência de compra,
        considerando a quantidade de ocorrências nas faturas.

        :return: Nome do produto mais frequente
        """
        items_df = self.df.explode("items", ignore_index=True)
        items_df = pd.json_normalize(items_df["items"])

        return items_df["product"].value_counts().idxmax()

    def total_spent_by_product(self) -> pd.Series:
        """
        Calcula o valor total gasto por cada produto.

        :return: Série pandas com o total gasto por produto
        """
        items_df = self.df.explode("items", ignore_index=True)
        items_df = pd.json_normalize(items_df["items"])

        items_df["total"] = items_df["quantity"] * items_df["unit_price"]

        return (
            items_df
            .groupby("product")["total"]
            .sum()
        )

    def product_listing(self) -> pd.DataFrame:
        """
        Retorna a lista de produtos contendo nome e preço unitário,
        removendo duplicidades.

        :return: DataFrame com produtos únicos e seus preços
        """
        items_df = self.df.explode("items", ignore_index=True)
        items_df = pd.json_normalize(items_df["items"])

        return (
            items_df[["product", "unit_price"]]
            .drop_duplicates()
            .reset_index(drop=True)
        )
