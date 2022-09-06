import pandas as pd 
from flask import Flask, jsonify

app = Flask(__name__)


# Contruindo funcionalidade
@app.route('/pegarvendas')
def pegarvendas():
    tabela = pd.read_csv('Tabela.csv')
    print(tabela)
    total_vendas = tabela['Vendas'].sum()
    resposta = {'total_vendas': total_vendas}
    return jsonify(resposta)
app.route()
