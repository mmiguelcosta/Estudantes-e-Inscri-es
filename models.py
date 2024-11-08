from database import db

class Estudante(db.Model):
    __tablename__ = 'estudante'
    id_estudante = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.Varchar(100))
    curso = db.Column(db.Varchar(100))

    def __init__(self, nome, curso):
        self.nome = nome
        self.curso = curso

    def __repr__(self):
        return f"<Estudante {self.nome}>"

class Inscricao(db.Model):
    __tablename__ = 'inscricao'
    id_inscricao = db.Column(db.Integer, primary_key=True)
    disciplina = db.Column(db.Varchar(100))
    semestre = db.Column(db.Varchar(10))
    id_estudante = db.Column(db.Integer, db.ForeignKey('estudante.id'))

    estudante = db.relationship('Estudante', foreign_keys=id_estudante)        

    def __init__(self, disciplina, semestre, id_estudante):
        self.disciplina = disciplina
        self.semestre = semestre
        self.id_estudante = id_estudante

    def __repr__(self):
        return f"<Inscrição {self.estudante.nome} - {self.disciplina} - {self.semestre} >"