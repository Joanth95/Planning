from flask import Flask, request, jsonify, session
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from werkzeug.security import generate_password_hash, check_password_hash
from config import Config
from models import db, Utilisateur, Agent, Cycle, Horaire, Absence
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return 'API Planning EHPAD opérationnelle !'

app.config.from_object(Config)
db.init_app(app)
CORS(app, supports_credentials=True)

with app.app_context():
    db.create_all()

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    if Utilisateur.query.filter_by(username=data['username']).first():
        return jsonify({'message': 'Utilisateur déjà existant.'}), 400
    hashed_pw = generate_password_hash(data['password'], method='pbkdf2:sha256')
    user = Utilisateur(username=data['username'], password_hash=hashed_pw, role=data.get('role', 'utilisateur'))
    db.session.add(user)
    db.session.commit()
    return jsonify({'message': 'Inscription réussie.'}), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    user = Utilisateur.query.filter_by(username=data['username']).first()
    if user and check_password_hash(user.password_hash, data['password']):
        session['user_id'] = user.id
        session['role'] = user.role
        return jsonify({'message': 'Connexion réussie.', 'role': user.role}), 200
    return jsonify({'message': 'Identifiants incorrects.'}), 401

@app.route('/logout', methods=['POST'])
def logout():
    session.clear()
    return jsonify({'message': 'Déconnexion réussie.'})

@app.route('/agents', methods=['GET', 'POST'])
def agents():
    if request.method == 'POST':
        data = request.json
        agent = Agent(
            nom=data['nom'],
            prenom=data['prenom'],
            poste=data.get('poste', ''),
            type_contrat=data.get('type_contrat', ''),
            cycle_id=data.get('cycle_id'),
            date_entree=datetime.strptime(data['date_entree'], "%Y-%m-%d").date() if data.get('date_entree') else None,
            date_sortie=datetime.strptime(data['date_sortie'], "%Y-%m-%d").date() if data.get('date_sortie') else None
        )
        db.session.add(agent)
        db.session.commit()
        return jsonify({'message': 'Agent ajouté.'}), 201
    agents = Agent.query.all()
    return jsonify([
        {
            'id': a.id, 'nom': a.nom, 'prenom': a.prenom, 'poste': a.poste,
            'type_contrat': a.type_contrat, 'cycle_id': a.cycle_id,
            'date_entree': a.date_entree.isoformat() if a.date_entree else '',
            'date_sortie': a.date_sortie.isoformat() if a.date_sortie else ''
        } for a in agents
    ])

# --------- AJOUT DE CETTE ROUTE POUR MODIFIER UN AGENT ------------
@app.route('/agents/<int:agent_id>', methods=['PUT'])
def update_agent(agent_id):
    data = request.json
    agent = Agent.query.get_or_404(agent_id)
    agent.nom = data.get('nom', agent.nom)
    agent.prenom = data.get('prenom', agent.prenom)
    agent.poste = data.get('poste', agent.poste)
    agent.type_contrat = data.get('type_contrat', agent.type_contrat)
    agent.cycle_id = data.get('cycle_id', agent.cycle_id)
    agent.date_entree = datetime.strptime(data['date_entree'], "%Y-%m-%d").date() if data.get('date_entree') else None
    agent.date_sortie = datetime.strptime(data['date_sortie'], "%Y-%m-%d").date() if data.get('date_sortie') else None
    db.session.commit()
    return jsonify({'message': 'Agent modifié.'})
# -----------------------------------------------------------------

@app.route('/cycles', methods=['GET', 'POST'])
def cycles():
    if request.method == 'POST':
        data = request.json
        cycle = Cycle(
            nom=data['nom'],
            structure_cycle=data['structure_cycle']
        )
        db.session.add(cycle)
        db.session.commit()
        return jsonify({'message': 'Cycle ajouté.'}), 201
    cycles = Cycle.query.all()
    return jsonify([
        {
            'id': c.id,
            'nom': c.nom,
            'structure_cycle': c.structure_cycle
        } for c in cycles
    ])

@app.route('/horaires', methods=['GET', 'POST'])
def horaires():
    if request.method == 'POST':
        data = request.json
        horaire = Horaire(
            nom=data.get('nom', ''),
            code=data.get('code', ''),
            heure_debut=data.get('heure_debut', ''),
            heure_fin=data.get('heure_fin', ''),
            pause=data.get('pause')
        )
        db.session.add(horaire)
        db.session.commit()
        return jsonify({'message': 'Horaire ajouté.'}), 201
    horaires = Horaire.query.all()
    return jsonify([
        {
            'id': h.id,
            'nom': h.nom,
            'code': h.code,
            'heure_debut': h.heure_debut,
            'heure_fin': h.heure_fin,
            'pause': h.pause
        } for h in horaires
    ])

@app.route('/absences', methods=['GET', 'POST'])
def absences():
    if request.method == 'POST':
        data = request.json
        absence = Absence(
            agent_id=data['agent_id'],
            date_debut=datetime.strptime(data['date_debut'], "%Y-%m-%d").date(),
            date_fin=datetime.strptime(data['date_fin'], "%Y-%m-%d").date(),
            motif=data.get('motif', ''),
            remplacant_id=data.get('remplacant_id')
        )
        db.session.add(absence)
        db.session.commit()
        return jsonify({'message': 'Absence ajoutée.'}), 201
    absences = Absence.query.all()
    return jsonify([
        {
            'id': a.id,
            'agent_id': a.agent_id,
            'date_debut': a.date_debut.isoformat(),
            'date_fin': a.date_fin.isoformat(),
            'motif': a.motif,
            'remplacant_id': a.remplacant_id
        } for a in absences
    ])

if __name__ == "__main__":
    app.secret_key = 'change-this-key'
    app.run(debug=True, port=5050)
