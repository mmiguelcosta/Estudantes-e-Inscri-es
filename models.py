from database import db

class Estudante(db.Model):
    __tablename__ = 'estudante'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    curso = db.Column(db.String(100))

    def __init__(self, nome, curso):
        self.nome = nome
        self.curso = curso

    def __repr__(self):
        return f"<Estudante {self.nome}>"

class Inscricao(db.Model):
    __tablename__ = 'inscricao'
    id = db.Column(db.Integer, primary_key=True)
    nome_disc = db.Column(db.String(100))
    semestre = db.Column(db.String(10))
    id_estudante = db.Column(db.Integer, db.ForeignKey('estudante.id'))

    estudante = db.relationship('Estudante', foreign_keys=id_estudante)        

    def __init__(self, disciplina, semestre, id_estudante):
        self.nome_disc = disciplina
        self.semestre = semestre
        self.id_estudante = id_estudante

    def __repr__(self):
        return f"<Inscrição {self.estudante.nome} - {self.nome_disc} - {self.semestre} >"