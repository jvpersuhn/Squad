import sys
<<<<<<< HEAD
sys.path.append('C:/Users/900152/Documents/Dados/Squad')
from flask import Flask, render_template, request
=======
sys.path.append('C:/Users/900143/Desktop/Squad')
from flask import Flask, render_template, request, redirect
>>>>>>> 6cb8ad78f30997bd43d876ef3a2c41a1643d1b2b
from controller.Front_controller import FrontController, FrontEnd
from controller.sgbd_controller import SGBD_controller, SGBD
<<<<<<< HEAD
=======
from controller.Back_controller import BackController, BackEnd
>>>>>>> 6cb8ad78f30997bd43d876ef3a2c41a1643d1b2b

app = Flask(__name__)

fc = FrontController()
bc = BackController()
sc = SGBD_controller()

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
    lista_sgbd = sc.select_all()
    return render_template('listarSgbd.html', lista = lista_sgbd)

@app.route('/excluirsgbd')
def excluirsgbd():
    return redirect('/listarSgbd')
    
@app.route('/excluirback')
def excluirback():
    return redirect('/listarBack')

@app.route('/excluirfront')
def excluirfront():
    return redirect('/listarFront')

@app.route('/salvarSGBD')
def salvarSGBD():
    nome = request.args['nome']
    descricao = request.args['descricao']
    versao = request.args['versao']
    sgbd = SGBD(0,nome,descricao,versao)
    sc.insert(sgbd)
    return redirect('/listarSgbd')

@app.route('/salvarFront')
def salvarFront():
    nome = request.args['nome']
    descricao = request.args['descricao']
    versao = request.args['versao']
    front = FrontEnd(0,nome,descricao,versao)
    fc.insert(front)
    return redirect('/listarFront')

@app.route('/salvarBack')
def salvarBack():
    nome = request.args['nome']
    descricao = request.args['descricao']
    versao = request.args['versao']
    back = BackEnd(0,nome,descricao,versao)
    bc.insert(back)
    return redirect('/listarBack')

@app.route('/cadastroSGBD')
def cadastroSGBD():
    return render_template('cadastroSGBD.html')

@app.route('/cadastroFront')
def cadastroFront():
    return render_template('cadastroFront.html')

@app.route('/cadastroBack')
def cadastroBack():
    return render_template('cadastroBack.html')


app.run(debug=True)