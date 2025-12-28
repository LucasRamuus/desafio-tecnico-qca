import json
from pathlib import Path
from models import Invoice


class InvoiceRepository:
    """
    Repositório responsável pela persistência das faturas em arquivo JSON.

    Funções principais:
    - Criar o arquivo de banco de dados caso não exista
    - Carregar e salvar dados no JSON
    - Evitar inserção de faturas duplicadas (Order ID)
    """

    def __init__(self, db_path: str = "database.json"):
        """
        Inicializa o repositório.

        :param db_path: Caminho do arquivo JSON usado como banco de dados.
        """
        self.db_path = Path(db_path)

        # Caso o arquivo ainda não exista, cria um JSON vazio
        if not self.db_path.exists():
            self._save([])

    def _load(self):
        """
        Carrega e retorna o conteúdo do arquivo JSON.

        :return: Lista de faturas armazenadas.
        """
        with open(self.db_path, "r", encoding="utf-8") as f:
            return json.load(f)

    def _save(self, data):
        """
        Salva os dados no arquivo JSON.

        :param data: Lista de faturas a serem persistidas.
        """
        with open(self.db_path, "w", encoding="utf-8") as f:
            json.dump(
                data,
                f,
                indent=4,
                ensure_ascii=False
            )

    def add_invoice(self, invoice: Invoice):
        """
        Adiciona uma nova fatura ao banco de dados.

        - Verifica se já existe uma fatura com o mesmo Order ID
        - Evita duplicidade de registros
        - Persiste os dados no formato JSON
        """
        data = self._load()

        # Evita salvar faturas duplicadas com o mesmo Order ID
        if any(inv["order_id"] == invoice.order_id for inv in data):
            return

        # Converte o modelo Pydantic para dicionário serializável em JSON
        data.append(invoice.model_dump(mode="json"))

        self._save(data)
