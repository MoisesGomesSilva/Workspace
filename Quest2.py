import pandas as pd

# Diretório CSV
file_path = "vendas.csv"
vendas_df = pd.read_csv(file_path)

# Converter a coluna de data e hora para o tipo datetime
vendas_df["data_hora"] = pd.to_datetime(vendas_df["data_hora"])

# Criar uma nova coluna com o nome do dia da semana
vendas_df["dia_semana"] = vendas_df["data_hora"].dt.day_name()

# Definir a ordem correta dos dias da semana (segunda a domingo)
ordem_dias = ["Monday", "Tuesday", "Wednesday", 'Thursday', "Friday", "Saturday", "Sunday"]

# Agrupamento por coluna 'dia_semana' e soma de qtd vendida
vendas_por_dia = vendas_df.groupby("dia_semana")["quantidade"].sum()

# Reordenar os resultados conforme a semana
vendas_por_dia = vendas_por_dia.reindex(ordem_dias)

# Painel de resultados
print("Distribuição total de vendas por dia da semana:")
print(vendas_por_dia)