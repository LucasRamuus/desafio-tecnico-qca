# Desafio Técnico QCA – Inovação e Desenvolvimento

Este projeto implementa uma automação em **Python 3.13** para processar faturas (Invoices) do setor financeiro de uma empresa.  
O objetivo é extrair dados de PDFs, armazená-los localmente e disponibilizar consultas analíticas.  

Dataset utilizado: [Company Documents Dataset](https://www.kaggle.com/datasets/ayoubcherguelaine/company-documents-dataset)

---

## Tecnologias

- **Python:** 3.13  
- **Bibliotecas utilizadas:**
  - `pandas` (análise de dados)  
  - `pydantic` (validação de dados)  
  - `pdfplumber` (leitura de PDFs)  

---

## Funcionalidades

- **Ingestão de Dados:**  
  - Ler múltiplos PDFs de uma pasta indicada.  
  - Extrair **Order ID**, **Data**, **Customer ID** e tabela de itens (**Produto, Quantidade e Preço Unitário**).

- **Armazenamento:**  
  - Salvar dados extraídos em `database.json`.  
  - Evitar duplicidade de **Order ID**.

- **Validação:**  
  - Garantir integridade dos dados usando **pydantic**.

- **Analytics:**  
  - Calcular e exibir:
    - Média do valor total das faturas  
    - Produto com maior frequência de compra  
    - Valor total gasto por cada produto  
    - Listagem de produtos (Nome e Preço Unitário)

---

## Regras importantes

- Bibliotecas obrigatórias: `pydantic`, `pandas`, `pdfplumber` ou `pypdf`.  
- Código orientado a objetos, separando **ingestão** e **análise**.  
- `database.json` **não deve ser versionado**; é criado e atualizado automaticamente.  

---

🚀 Instalação e Configuração do Projeto
📌 Pré-requisitos

Antes de iniciar, certifique-se de ter instalado em sua máquina:

Python 3.13 ou superior
👉 Verifique com: python --version

📥 Clonando o Repositório

Clone o projeto para sua máquina local: 
```bash
git clone https://github.com/LucasRamuus/desafio-tecnico-qca.git
```

📦 Instalação das Dependências

```bash
cd desafio-tecnico-qca
```

Instale todas as bibliotecas necessárias utilizando o arquivo requirements.txt: 
```bash
pip install -r requirements.txt
```

📂 Estrutura de Entrada dos Dados

Utilize a pasta destinada aos arquivos PDF.

Coloque dentro dela todos os PDFs de faturas que deseja processar.

▶️ Execução do Projeto

Para iniciar o programa, execute: 
```bash
python main.py
```

📊 Exemplo de Saída no Console
```bash
Média do valor total das faturas: 1372.13

Produto com maior frequência de compra: Manjimup Dried Apples

Valor total gasto por cada produto:
 - Jack's New England Clam Chowder: 77.00
 - Louisiana Fiery Hot Pepper Sauce: 252.00
 - Manjimup Dried Apples: 3180.00
 - Mozzarella di Giovanni: 174.00
 - Queso Cabrales: 168.00
 - Singaporean Hokkien Fried Mee: 98.00
 - Tofu: 167.40

Lista de produtos (Nome e Preço Unitário):
 - Queso Cabrales: 14.00
 - Singaporean Hokkien Fried Mee: 9.80
 - Mozzarella di Giovanni: 34.80
 - Jack's New England Clam Chowder: 7.70
 - Manjimup Dried Apples: 42.40
 - Louisiana Fiery Hot Pepper Sauce: 16.80
 - Tofu: 18.60
