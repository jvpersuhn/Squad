import sys
sys.path.append('C:/Users/900143/Desktop/Squad')
from flask import Flask, render_template, request, redirect
from controller.Front_controller import FrontController, FrontEnd
from controller.sgbd_controller import SGBD_controller, SGBD
from controller.Back_controller import BackController, BackEnd
from controller.squad_controller import SquadController, Squad


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
    lista_squad = sqc.select_all()
    return render_template('listarSquads.html',lista = lista_squad)

@app.route('/excluirSquad')
def excluir_squad():
    id = int(request.args['id'])
    sqc.delete(id)
    return redirect('/listarSquads.html')

@app.route('/excluirsgbd')
def excluirsgbd():
    id = int(request.args['id'])
    sc.delete(id)
    return redirect('/listarSgbd')
    
@app.route('/excluirback')
def excluirback():
    id = int(request.args['id'])
    bc.delete(id)
    return redirect('/listarBack')

@app.route('/excluirfront')
def excluirfront():
    id = int(request.args['id'])
    fc.delete(id)
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
        s.id_sgbd = int(request.args['sgbd'])
    if request.args['frameFront'] != 'Null':
        s.id_linguagemFront = int(request.args['frameFront'])
    if request.args['linguagemBack'] != 'Null':
        s.id_linguagemBack = int(request.args['linguagemBack'])
    
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
    squad = Squad(0,'','','')
    if 'id' in request.args:
        squad = sqc.select_byId(request.args['id'])
    ls = sc.select_all()
    lf = fc.select_all()
    lb = bc .select_all()
    return render_template('cadastroSquad.html', lista_sgbd = ls, lista_front = lf, lista_back = lb, squad = squad)

app.run(debug=True)