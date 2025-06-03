from app import app
from models import db, Horaire

horaires = [
    {"nom": "E7AB",   "code": "E7AB",   "heure_debut": "07:00", "heure_fin": "19:00", "pause": 2},
    {"nom": "E7CD",   "code": "E7CD",   "heure_debut": "07:00", "heure_fin": "19:00", "pause": 2},
    {"nom": "E8AB",   "code": "E8AB",   "heure_debut": "08:00", "heure_fin": "20:00", "pause": 2},
    {"nom": "E8CD",   "code": "E8CD",   "heure_debut": "08:00", "heure_fin": "20:00", "pause": 2},
    {"nom": "UP17",   "code": "UP17",   "heure_debut": "07:00", "heure_fin": "19:00", "pause": 2},
    {"nom": "UP18",   "code": "UP18",   "heure_debut": "08:00", "heure_fin": "20:00", "pause": 2},
    {"nom": "UP27",   "code": "UP27",   "heure_debut": "07:00", "heure_fin": "19:00", "pause": 2},
    {"nom": "UP28",   "code": "UP28",   "heure_debut": "08:00", "heure_fin": "20:00", "pause": 2},
    {"nom": "AJ",     "code": "AJ",     "heure_debut": "09:30", "heure_fin": "17:30", "pause": 0.5},
    {"nom": "IDE",    "code": "IDE",    "heure_debut": "07:00", "heure_fin": "19:00", "pause": 2},
    # Les trois postes de nuit
    {"nom": "N1",     "code": "N1",     "heure_debut": "18:45", "heure_fin": "06:45", "pause": 2},
    {"nom": "N2",     "code": "N2",     "heure_debut": "19:15", "heure_fin": "07:15", "pause": 2},
    {"nom": "N3",     "code": "N3",     "heure_debut": "19:15", "heure_fin": "07:15", "pause": 2},
]

with app.app_context():
    for h in horaires:
        if not Horaire.query.filter_by(nom=h["nom"]).first():
            horaire = Horaire(**h)
            db.session.add(horaire)
    db.session.commit()
    print("✅ Horaires ajoutés en base !")
