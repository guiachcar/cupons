from app import db

class Cupom(db.Model):
	__tablename__ = 'cupoms'
	_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	nome = db.Column(db.String(100))
	email = db.Column(db.String(100), unique=True)
	valor = db.Column(db.Float())
    
	def __init__(self, nome, email, valor):
		self.nome = nome
		self.email = email
		self.valor = valor
	def save(self):
		db.session.add(self)
		return db.session.commit()

db.create_all()
