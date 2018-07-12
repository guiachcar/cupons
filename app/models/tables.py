from app import db

class Cupom(db.Model):
	__tablename__ = 'cupoms'
	_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	nome = db.Column(db.String(100))
	email = db.Column(db.String(100))
	valor = db.Column(db.Float())
	id_compra = db.Column(db.Integer(), nullable=True)
    
	def __init__(self, nome, email, valor, id_compra):
		self.nome = nome
		self.email = email
		self.valor = valor
		self.id_compra = id_compra
	def save(self):
		db.session.add(self)
		return db.session.commit()

db.create_all()
