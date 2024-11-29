from flask import Blueprint, render_template, request, redirect, flash
from models import Inscricao, Estudante
from database import db

bp_inscricoes = Blueprint('inscricao', __name__, template_folder="templates")

@bp_inscricoes.route("/")
def index():
    i = Inscricao.query.all()
    return render_template("inscricoes.html", dados=i)


@bp_inscricoes.route("/add")
def add():
    i = Inscricao.query.all()
    e = Estudante.query.all()
    return render_template("inscricoes_add.html", dados=i, estudantes=e)


@bp_inscricoes.route("/save", methods=['POST'])
def save():
    nome_disc = request.form.get("nome_disc")
    semestre = request.form.get("semestre")
    id_estudante = request.form.get("id_estudante")

    id_estudante = Estudante.query.all()

    if nome_disc and semestre and id_estudante:
        db_inscricao = Inscricao(nome_disc, semestre, id_estudante)
        db.session.add(db_inscricao)
        db.session.commit()
        flash("Inscrição cadastrada!")
        return redirect("/inscricoes")
    else:
        flash("Preencha todos os campos!")
        return redirect("/inscricoes/add")
    

@bp_inscricoes.route("/remove/<int:id>")
def remove(id):
    i = Inscricao.query.get(id)
    try:
        db.session.delete(i)
        db.session.commit()
        flash("inscricao removida!")
    except:
        flash("Inscricao Inválida!")
    return redirect("/inscricoes")


@bp_inscricoes.route("/edit/<int:id>")
def edit(id):
    i = Inscricao.query.get(id)
    e = Estudante.query.all()
    return render_template("inscricoes_edit.html", dados=i, estudantes=e)


@bp_inscricoes.route("/edit-save", methods=['POST'])
def edit_save():
    nome_disc = request.form.get("nome_disc")
    semestre = request.form.get("semestre")
    id_estudante = request.form.get("id_estudante")
    id = request.form.get("id")
    if nome_disc and semestre and id_estudante and id:
        i = Inscricao.query.get(id)
        i.nome_disc = nome_disc
        i.semestre = semestre
        i.id_estudante = id_estudante
        db.session.commit()
        flash("Dados atualizados!")
    else:
        flash("Preencha todos os campos!")
    return redirect("/inscricoes")