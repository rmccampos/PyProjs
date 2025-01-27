# -*- coding: utf-8 -*-
"""Dia1.ipynb
Automatically generated by Colab.
Original file is located at
	https://colab.research.google.com/drive/1yKUbWwH9DFgg6v_N1UkAIkZSq20X4rqc
"""

import pandas as pd
import os

caminho = '/content/drive/MyDrive/Colab Notebooks/Dia 1'
extensao = '.csv'

arquivo = [arquivo for arquivo in os.listdir(caminho) if arquivo.endswith(extensao)]

dfs = []
for arquivo in arquivo:
    df = pd.read_csv(os.path.join(caminho, arquivo))
    dfs.append(df)

df = pd.concat(dfs, ignore_index=True)

df.info()

df.drop_duplicates(inplace=True)
df.info()
df.dropna()

acervo = pd.read_parquet('/content/drive/MyDrive/Colab Notebooks/Dia 1/dados_exemplares.parquet')
dados = pd.merge(df, acervo, on='codigo_barras')
dados.dropna(inplace=True)
dados.reset_index(inplace=True, drop=True)
dados.head()
