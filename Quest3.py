import pandas as pd

# Diretório CSV
vendas_df = pd.read_csv("vendas.csv")
produtos_df = pd.read_csv("produtos.csv")

# Converter a coluna de data e hora para datetime
vendas_df["data_hora"] = pd.to_datetime(vendas_df["data_hora"])

# Filtro de vendas no mês de outubro de 2024
vendas_outubro = vendas_df[
    (vendas_df["data_hora"].dt.year == 2024) & 
    (vendas_df["data_hora"].dt.month == 10)
]

# Mescla de dados de produtos para obter categoria e preço
vendas_outubro = vendas_outubro.merge(
    produtos_df[["id_produto", "categoria", "preco_revenda"]],
    on="id_produto",
    how="left"
)

# Cálculo do valor total da venda por linha (qtd * preço unit.)
vendas_outubro["valor_total"] = vendas_outubro["quantidade"] * vendas_outubro["preco_revenda"]

# Agrupamento por categoria e cálculo total vendido e número de vendas únicas
resumo_categoria = vendas_outubro.groupby("categoria").agg({
    "valor_total": "sum",
    "id_venda": "nunique"
}).rename(columns={
    "valor_total": "valor_total_reais",
    "id_venda": "quantidade_vendas_unicas"
})

# Ordem de categorias com maior valor de vendas
resumo_categoria = resumo_categoria.sort_values(by="valor_total_reais", ascending=False)

# Painel de resultados
print(resumo_categoria)