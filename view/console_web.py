import sys
sys.path.append('C:/Users/900152/Documents/Dados/Squad')
from flask import Flask, render_template, request, redirect
from controller.Front_controller import FrontController, FrontEnd
from controller.sgbd_controller import SGBD_controller, SGBD
<<<<<<< HEAD
from controller.Back_controller import BackController
=======
<<<<<<< HEAD
=======
from controller.Back_controller import BackController, BackEnd
<<<<<<< HEAD
from controller.squad_controller import SquadController, Squad
=======
>>>>>>> 6cb8ad78f30997bd43d876ef3a2c41a1643d1b2b
>>>>>>> 1d7ee4134c40188f5ce44a438adf59dc0da6cb97

>>>>>>> c2596d73789635e7fa4f7a87d41550ab5354c79b
app = Flask(__name__)

fc = FrontController()
bc = BackController()
sc = SGBD_controller()
sqc = SquadController()

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

@app.route('/listarSquads')
def listar_squads():
    return render_template('listarSquads.html')

@app.route('/excluirsgbd')
def excluirsgbd():
    return redirect('/listarSgbd')

@app.route('/alterarsgbd')
def alterarasgbd():
    return redirect('/listarSgbd')
    
@app.route('/excluirback')
def excluirback():
    return redirect('/listarBack')

@app.route('/alterarback')
def alterarBack():
    return redirect('/listarBack')

@app.route('/excluirfront')
def excluirfront():
    return redirect('/listarFront')

@app.route('/alterarfront')
def alterarfront():
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

@app.route('/salvarSquad')
def salvarSquad():
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        id = 0
    nome = request.args['nomeSquad']
    desc = request.args['descricao']
    if 'qtdPessoas' in request.args:
        qtdPessoas = int(request.args['qtdPessoas'])
    else:
        qtdPessoas = 0
    s = Squad(id,nome, desc, qtdPessoas)

    if request.args['sgbd'] != 'Null':
        s.sgbd = int(request.args['sgbd'])
    if request.args['frameFront'] != 'Null':
        s.linguagemFront = int(request.args['frameFront'])
    if request.args['linguagemBack'] != 'Null':
        s.linguagemBack = int(request.args['linguagemBack'])
    
    sqc.insert(s)

    return redirect('/')

@app.route('/cadastroSGBD')
def cadastroSGBD():
    return render_template('cadastroSGBD.html')

@app.route('/cadastroFront')
def cadastroFront():
    return render_template('cadastroFront.html')

@app.route('/cadastroBack')
def cadastroBack():
    return render_template('cadastroBack.html')

@app.route('/cadastroSquad')
def cadastroSquad():
    ls = sc.select_all()
    lf = fc.select_all()
    lb = bc.select_all()
    return render_template('cadastroSquad.html', lista_sgbd = ls, lista_front = lf, lista_back = lb)


app.run(debug=True)