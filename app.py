from flask import Flask, render_template
app = Flask(__name__)
app.config['SECRET_KEY'] = 'Senhazaza'
conexao = "mysql+pymysql://alunos:cefetmg@127.0.0.1/estud"
app.config['SQLALCHEMY_DATABASE_URI'] = conexao
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
from database import db
from flask_migrate import Migrate
db.init_app(app)
migrate = Migrate(app, db)
from models import Estudante, Inscricao
from modulos.estudantes.estudantes import bp_estudantes
app.register_blueprint(bp_estudantes, url_prefix='/estudantes')


from modulos.inscricoes.inscricoes import bp_inscricoes
app.register_blueprint(bp_inscricoes, url_prefix='/inscricoes')

@app.route('/')
def index():
    return render_template('ola.html')