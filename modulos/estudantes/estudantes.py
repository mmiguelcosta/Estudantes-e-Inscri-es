from flask import Blueprint, render_template, request, redirect, flash
from models import Estudante
from database import db

bp_estudantes = Blueprint('estudantes', __name__, template_folder="templates")

@bp_estudantes.route("/")
def index():
    e = Estudante.query.all()
    return render_template("estudantes.html", dados=e)


@bp_estudantes.route("/add")
def add():
    return render_template("estudantes_add.html")


@bp_estudantes.route("/save", methods=['POST'])
def save():
    nome = request.form.get("nome")
    curso = request.form.get("curso")
    if nome and curso:
        db_estudante = Estudante(nome, curso)
        db.session.add(db_estudante)
        db.session.commit()
        flash("estudante cadastrado!")
        return redirect("/estudantes")
    else:
        flash("Preencha todos os campos!")
        return redirect("/estudantes/add")
    

@bp_estudantes.route("/remove/<int:id>")
def remove(id):
    e = Estudante.query.get(id)
    try:
        db.session.delete(e)
        db.session.commit()
        flash("estudante removido!")
    except:
        flash("estudante Inválido!")
    return redirect("/estudantes")


@bp_estudantes.route("/edit/<int:id>")
def edit(id):
    e = Estudante.query.get(id)
    return render_template("estudantes_edit.html", dados=e)


@bp_estudantes.route("/edit-save", methods=['POST'])
def edit_save():
    nome = request.form.get("nome")
    curso = request.form.get("curso")
    id = request.form.get("id")
    if nome and curso and id:
        e = Estudante.query.get(id)
        e.nome = nome
        e.curso = curso
        db.session.commit()
        flash("Dados atualizados!")
    else:
        flash("Preencha todos os campos!")
    return redirect("/estudantes")