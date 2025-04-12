import pandas as pd

# Diretório CSV
file_path = "estoque.csv"

# Load values
df = pd.read_csv(file_path)

# Calculo estoque médio diário p/ produto (considerando todas as lojas)
media_estoque = df.groupby('id_produto')['quantidade_estoque'].mean()

# Ordem e seleção dos 5 produtos com maior estoque médio
top_5_produtos = media_estoque.sort_values(ascending=False).head(5)

# Painel de resultados
print("Top 5 produtos com maior estoque médio diário:")
print(top_5_produtos)