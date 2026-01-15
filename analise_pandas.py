
import pandas as pd
import numpy as np

# --- 1. SIMULAÇÃO DA CARGA DE DADOS ---
dados_vendas = {
    'id_pedido': [101, 102, 103, 104, 105, 106],
    'data_venda': ['2025-01-10', '2025-01-11', '12/01/2025', '2025-01-12', '2025-01-13', '2025-01-14'], # Formatos misturados
    'produto': ['Notebook', 'Mouse', 'Teclado', 'Notebook', 'Monitor', 'Mouse'],
    'categoria': ['Eletrônicos', 'Periféricos', 'Periféricos', 'Eletrônicos', 'Eletrônicos', 'Periféricos'],
    'qtd': [1, 5, 2, 1, 2, -1], # Nota: -1 indica uma devolução
    'preco_unitario': [3500.00, 50.00, 100.00, 3500.00, 800.00, 50.00]
}

df = pd.DataFrame(dados_vendas)

print("--- Dados Brutos ---")
print(df.head())

# --- 2. LIMPEZA DE DADOS (Data Cleaning) ---
# Problema: Datas em formatos diferentes (ISO e BR)
# Solução: to_datetime com 'dayfirst=True' ajuda, mas o ideal é forçar erros='coerce' e tratar
df['data_venda'] = pd.to_datetime(df['data_venda'], dayfirst=True, errors='coerce')

# Problema: Devoluções (qtd negativa) atrapalham a soma de vendas brutas
# Solução: Separar devoluções ou filtrar.
df['tipo_movimento'] = np.where(df['qtd'] < 0, 'Devolução', 'Venda')

# --- 3. ENRIQUECIMENTO ---

# Criando coluna de Faturamento Total (Qtd * Preço)
# Para devoluções, o valor ficará negativo, o que abate do faturamento
df['faturamento_total'] = df['qtd'] * df['preco_unitario']

# Extraindo Mês e Dia da Semana para análise de sazonalidade
df['mes'] = df['data_venda'].dt.month_name()
df['dia_semana'] = df['data_venda'].dt.day_name()

# --- 4. ANÁLISE EXPLORATÓRIA ---
# Insight 1: Qual categoria dá mais dinheiro?
analise_categoria = df[df['tipo_movimento'] == 'Venda'].groupby('categoria')['faturamento_total'].sum()

print("\n--- Faturamento por Categoria (Só Vendas Válidas) ---")
print(analise_categoria)

# Insight 2: Ticket Médio (Quanto cada venda traz em média?)
ticket_medio = df[df['tipo_movimento'] == 'Venda']['faturamento_total'].mean()
print(f"\nTicket Médio: R$ {ticket_medio:.2f}")