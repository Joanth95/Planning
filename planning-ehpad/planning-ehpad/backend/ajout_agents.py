import requests

# L’URL de ton backend Flask
URL = "http://localhost:5050/agents"

agents = [
    {"nom": "KOFFI", "prenom": "Marie Noelle", "poste": "ASDE / ASG", "type_contrat": "CDI"},
    {"nom": "RAMINOARISON", "prenom": "Tahinjanahary", "poste": "AVS - VAE", "type_contrat": "CDI"},
    {"nom": "BOUGLOUF", "prenom": "Fatima", "poste": "AVS - VAE", "type_contrat": "CDI"},
    {"nom": "PFISTER", "prenom": "Andrée", "poste": "AVS - VAE", "type_contrat": "CDI"},
    {"nom": "DUPONT", "prenom": "Céline", "poste": "AVS - VAE", "type_contrat": "CDI"},
    {"nom": "LAMBARATE", "prenom": "Maryem", "poste": "AVS - VAE", "type_contrat": "CDD"},
    {"nom": "HOTTIER", "prenom": "LISA", "poste": "ASDE", "type_contrat": "CDD / APP"},
    {"nom": "HOUPIN", "prenom": "Sophie", "poste": "AVS - VAE", "type_contrat": "CDI"},
    {"nom": "PREMERSDORFER", "prenom": "Marie-Laure", "poste": "AVS - VAE", "type_contrat": "CDI"},
    {"nom": "SEURON", "prenom": "Nathalie", "poste": "AVS - VAE", "type_contrat": "CDI"},
    {"nom": "MATUSIAK", "prenom": "Mélissa", "poste": "AVS - VAE", "type_contrat": "CDI"},
    {"nom": "FRUMINET", "prenom": "Alice", "poste": "AVS - VAE", "type_contrat": "CDI"},
    {"nom": "SALM", "prenom": "Kelly", "poste": "ASDE", "type_contrat": "CDD"},
    {"nom": "BOILAN", "prenom": "Aurore", "poste": "AVS - VAE", "type_contrat": "CDI"},
    {"nom": "SCHERER", "prenom": "Emmanuelle", "poste": "ASDE / ASG", "type_contrat": "CDI"},
    {"nom": "LOPEZ", "prenom": "Aude", "poste": "ASDE / ASG", "type_contrat": "CDI"},
    {"nom": "WIERZBICKI", "prenom": "Catherine", "poste": "IDE", "type_contrat": "CDI"},
    {"nom": "DJELOUL", "prenom": "Walida", "poste": "IDE", "type_contrat": "CDD"},
    {"nom": "ALLEGRE", "prenom": "Fanny", "poste": "IDER", "type_contrat": "CDI"},
    {"nom": "THIRIET", "prenom": "Cassandra", "poste": "AVS - VAE", "type_contrat": "CDI"},
    {"nom": "RANDAZZO", "prenom": "Sandrine", "poste": "ASDE", "type_contrat": "CDI"},
    {"nom": "KADDAR", "prenom": "Nordine", "poste": "AVS - VAE", "type_contrat": "CDI"},
    {"nom": "BITOUNDI", "prenom": "Murcile", "poste": "ASDE", "type_contrat": "CDI"},
    {"nom": "SERY", "prenom": "Mirelle", "poste": "AVS - VAE", "type_contrat": "CDD"}
]

for agent in agents:
    response = requests.post(URL, json=agent)
    if response.status_code == 201:
        print(f"Ajouté : {agent['prenom']} {agent['nom']}")
    else:
        print(f"Erreur pour : {agent['prenom']} {agent['nom']} - {response.text}")
