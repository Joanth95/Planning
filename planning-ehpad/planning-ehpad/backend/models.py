from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Utilisateur(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)
    role = db.Column(db.String(20), default='utilisateur')

class Agent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(80), nullable=False)
    prenom = db.Column(db.String(80), nullable=False)
    poste = db.Column(db.String(80))
    type_contrat = db.Column(db.String(80))
    cycle_id = db.Column(db.Integer, db.ForeignKey('cycle.id'))
    date_entree = db.Column(db.Date)
    date_sortie = db.Column(db.Date, nullable=True)

class Cycle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(80))
    structure_cycle = db.Column(db.String(120))

class Horaire(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(80))
    code = db.Column(db.String(10))
    heure_debut = db.Column(db.String(5))
    heure_fin = db.Column(db.String(5))
    pause = db.Column(db.Float)

class Absence(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    agent_id = db.Column(db.Integer, db.ForeignKey('agent.id'))
    date_debut = db.Column(db.Date)
    date_fin = db.Column(db.Date)
    motif = db.Column(db.String(80))
    remplacant_id = db.Column(db.Integer, db.ForeignKey('agent.id'), nullable=True)
