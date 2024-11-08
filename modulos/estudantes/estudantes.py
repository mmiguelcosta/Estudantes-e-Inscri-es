from flask import Blueprint, render_template, request, redirect, flash
from database import db
from models import Estudante

bp_estudante = Blueprint('estudantes', __name__, template_folder='templates')

@bp_estudante.route('/')
def index():
    dados = Estudante.query.all()
    return render_template('estudante.html', dados=dados)

@bp_estudante.route('/add')
def add():
    return render_template('estudante_add.html')

@bp_estudante.route('/save', methods=['POST'])
def save():
    nome = request.form.get('nome')
    email = request.form.get('email')
    senha = request.form.get('senha')
    if nome and email and senha:
        objeto = Estudante(nome, email, senha)
        db.session.add(objeto)
        db.session.commit()
        flash('Estudante salvo')
        return redirect('/estudantes')
    else:
        flash('Preencha todos os campos')
        return redirect('/estudantes/add')


