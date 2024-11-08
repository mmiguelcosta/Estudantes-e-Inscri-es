from flask import Blueprint, render_template, request, redirect, flash
from database import db
from models import Estudante, Inscricao

bp_inscricao = Blueprint('inscricoes', __name__, template_folder='templates')

@bp_inscricao.route('/')
def index():
    i = Inscricao.query.all()
    return render_template('pedido.html', inscricoes=i)

@bp_inscricao.route('/add')
def add():
    e = Estudante.query.all()
    return render_template('pedido_add.html', estudantes=e)

@bp_inscricao.route('/save', methods=['POST'])
def save():
    id_estudante = request.form.get('id_estudante')
    id_inscricao = request.form.get('pizza_id')
    data = request.form.get('data')
    if id_estudante and id_inscricao and data:
        objeto = Inscricao(id_estudante, id_inscricao, data)
        db.session.add(objeto)
        db.session.commit()
        flash('pedido salvo')
        return redirect('/inscricoes')
    else:
        flash('Preencha todos os campos')
        return redirect('/inscricoes/add')


