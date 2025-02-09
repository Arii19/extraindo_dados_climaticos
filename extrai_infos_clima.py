import os
from os.path import join
import pandas as pd
from datetime import datetime, timedelta

# intervalo de datas
data_inicio = datetime.today()
data_fim = data_inicio + timedelta(days=7)

# formatando as datas para pegar mês ano e dia
data_inicio = data_inicio.strftime('%Y-%m-%d')
data_fim = data_fim.strftime('%Y-%m-%d')

city = 'Adamantina'
key = '7JCBNS69BDJQ4B7A6LZ8GRZP5'

URL = join('https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/',
    f'{city}/{data_inicio}/{data_fim}?unitGroup=metric&include=days&key={key}&contentType=csv') #definir parametros que os dados venham

#Declarando a variavel, em que os daods vem do url anterior
dados = pd.read_csv(URL)
print(dados.head())

#caminho para a geração do CSV - Aletrar se usar em outro PC
file_path = r"C:\Users\Microsoft\Documents\PYTHON\extra-_dados_climaticos\semana01"
os.mkdir(file_path)

dados.to_csv(file_path + 'dados_brutos.csv')
dados[['datetime','tempmin', 'temp', 'tempmax']].to_csv(file_path + 'temperaturas.csv')
dados[['datetime', 'description', 'icon']].to_csv(file_path + 'condicoes.csv')

