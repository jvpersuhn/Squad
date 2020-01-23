import sys
sys.path.append('C:/Users/900143/Desktop/Squad')
from flask import Flask, render_template, request
from controller.Front_controller import FrontController, FrontEnd
from controller.Back_controller import BackController, BackEnd
from controller.sgbd_controller import SGBD_controller, SGBD
<<<<<<< HEAD
=======



>>>>>>> 3c5d97bbcb3943e409a4d7f8e1d667cf30fb4280

app = Flask(__name__)

fc = FrontController()
bc = BackController()
sgbdc = SGBD_controller()

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

@app.route('/listarSgbd')
def listar_sgbd():
    lista_sgbd = sgbdc.select_all()
    return render_template('listarSgbd.html', lista = lista_sgbd)

@app.route('/excluir')
def excluir():
    id = (request.args['id'])
    
    


app.run(debug=True)