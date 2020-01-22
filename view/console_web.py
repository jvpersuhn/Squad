import sys
sys.path.append('C:/Users/900152/Documents/Dados/Squad')

from flask import Flask, render_template, request
from model.frontend import FrontEnd
from controller.Front_controller import FrontController
from model.backend import BackEnd
from controller.Back_controller import BackController
app = Flask(__name__)

fc = FrontController()
bc = BackController()

@app.route('/')
def principal():
    return render_template('index.html')
@app.route('/listarFront')
def listar_front():
    lista_front = fc.select_all()
    return render_template('listarFront.html', lista = lista_front)

@app.route('/listarBack')
def listar_back():
    lista_back = bc.select_all()
    return render_template('ListarBack.html', lista = lista_back)



app.run(debug=True)