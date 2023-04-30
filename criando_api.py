'''projeto basico com flask para entendimento do curso de python
'''
from random import choice
from json import loads
from pandas import DataFrame, read_csv
from flask import jsonify, Flask  # , request
from flask_ngrok import run_with_ngrok

app = Flask(__name__)
run_with_ngrok(app)  # Start ngrok when app is run

dfcsv_dados = read_csv('dados.csv', delimiter=';')
dados_str_json = dfcsv_dados.to_json(orient='records')
#  ).replace('[', '{"data": [').replace(']', ']}')
dict_dados = loads(dados_str_json)

#  exemplo de dados se considerar a linha 14 com replace, se necessario
d2 = {'data': [
    {'Number': 1, 'Name': 'Mahesh', 'Age': 25,
     'City': 'Bangalore', 'Country': 'India'},
    {'Number': 2, 'Name': 'Alex', 'Age': 26,
     'City': 'London', 'Country': 'UK'},
    {'Number': 3, 'Name': 'Davi', 'Age': 27,
     'City': 'San Francisco', 'Country': 'USA'},
    {'Number': 4, 'Name': 'John', 'Age': 28,
     'City': 'Toronto', 'Country': 'Canada'},
    {'Number': 5, 'Name': 'Chris', 'Age': 29,
     'City': 'Paris', 'Country': 'France'}
    ]}
# print(type(d), f'd: {d}\n\n')
# print(type(d2), f'd2: {d2}\n\n')


@app.route('/')
def home():
    '''famoso Hello World'''
    return "<marquee><h3> TO CHECK IN PUT ADD '/input' TO THE\
      URL AND TO CHECK OUT PUT ADD '/output' TO THE URL.</h3></marquee>"


@app.route('/index')
def finput():
    '''retorna o dict'''
    return jsonify(dict_dados)


@app.route('/output', methods=['GET', 'POST'])
def pred_json():
    '''pagina de saida'''
    pred = choice(['positive', 'negative'])
    new_d = dict_dados
    new_d['prediction'] = pred
    return jsonify(new_d)


def return_planilha(data: dict) -> DataFrame:
    '''funcao definida para gerar a planilha de retorno com o pandas'''
    return DataFrame(data)


# print(return_planilha(dict_dados))
app.run()
