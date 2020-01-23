import sys
sys.path.append('C:/Users/900152/Documents/Dados/Squad')
from flask import Flask, render_template, request, redirect
from controller.Front_controller import FrontController, FrontEnd
from controller.Back_controller import BackController, BackEnd
from controller.sgbd_controller import SGBD_controller, SGBD




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
    aaa = sgbdc.select_all()
    return render_template('listarSgbd.html', a = aaa)


@app.route('/excluirsgbd')
def excluirsgbd():
    return redirect('/listarSgbd')
    
@app.route('/excluirback')
def excluirback():
    return redirect('/listarBack')

@app.route('/excluirfront')
def excluirfront():
    return redirect('/listarFront')


app.run(debug=True)