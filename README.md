# Análise de Vendas e Tratamento de Dados (ETL) 📊

Este projeto executa um pipeline de dados focado na etapa de **Limpeza e Transformação**. O objetivo é simular o tratamento de uma base de vendas "suja" (com erros de cadastro, tipos incorretos e nulos) transformando-a em insights confiáveis.

## 🎯 Objetivo
Demonstrar competências técnicas em **Engenharia de Dados** e **Análise**, com foco na manipulação de DataFrames, correção de inconsistências e preparação de dados para Dashboards.

## 🛠️ Tecnologias Utilizadas
* **Python (Pandas/NumPy):** Para limpeza (Data Cleaning), imputação de valores nulos e tipagem de dados.
* **SQL:** Consultas analíticas para relatórios de faturamento e segmentação (Joins, Case When, Group By).
* **Simulação de Dados:** Criação de datasets fictícios que imitam problemas reais do dia a dia (datas desformatadas, duplicatas).
* **Feature Engineering:** Criação de novas métricas de negócio (Ticket Médio, Sazonalidade).

## 📂 Estrutura do Projeto
1.  `analise_pandas.py`: Script que processa a base de dados bruta, aplica regras de negócio para limpeza e gera as métricas finais.
2.  `queries_sql.sql`: Demonstração de consultas SQL otimizadas para análise de performance de vendas.

## 🚀 Como Executar
Para rodar o script de análise:
```bash
pip install pandas
python analise_pandas.py
