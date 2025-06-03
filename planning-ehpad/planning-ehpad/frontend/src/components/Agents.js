import React, { useState, useEffect } from 'react';

function Agents() {
  const [agents, setAgents] = useState([]);
  const [form, setForm] = useState({ nom: '', prenom: '', poste: '', type_contrat: '', date_entree: '', date_sortie: '' });
  const [editingId, setEditingId] = useState(null);

  // Récupérer la liste des agents
  const fetchAgents = () => {
    fetch('http://localhost:5050/agents')
      .then(res => res.json())
      .then(data => setAgents(data));
  };

  useEffect(() => {
    fetchAgents();
  }, []);

  const handleChange = e => setForm({ ...form, [e.target.name]: e.target.value });

  // Ajout ou modification
  const handleSubmit = e => {
    e.preventDefault();
    if (editingId) {
      // Modification d'agent
      fetch(`http://localhost:5050/agents/${editingId}`, {
        method: "PUT",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(form)
      })
        .then(res => res.json())
        .then(() => {
          setForm({ nom: '', prenom: '', poste: '', type_contrat: '', date_entree: '', date_sortie: '' });
          setEditingId(null);
          fetchAgents();
        });
    } else {
      // Ajout d'agent
      fetch('http://localhost:5050/agents', {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(form)
      })
        .then(res => res.json())
        .then(() => {
          setForm({ nom: '', prenom: '', poste: '', type_contrat: '', date_entree: '', date_sortie: '' });
          fetchAgents();
        });
    }
  };

  // Lancer la modification
  const handleEdit = (agent) => {
    setForm({
      nom: agent.nom || '',
      prenom: agent.prenom || '',
      poste: agent.poste || '',
      type_contrat: agent.type_contrat || '',
      date_entree: agent.date_entree || '',
      date_sortie: agent.date_sortie || ''
    });
    setEditingId(agent.id);
  };

  // Annuler l’édition
  const handleCancel = () => {
    setForm({ nom: '', prenom: '', poste: '', type_contrat: '', date_entree: '', date_sortie: '' });
    setEditingId(null);
  };

  // Tri : agents sortis à la fin
  const sortedAgents = [...agents].sort((a, b) => {
    if (!a.date_sortie && b.date_sortie) return -1;
    if (a.date_sortie && !b.date_sortie) return 1;
    return a.nom.localeCompare(b.nom);
  });

  return (
    <div>
      <h2>Gestion des agents</h2>
      <form onSubmit={handleSubmit} style={{ marginBottom: '1em' }}>
        <input name="nom" placeholder="Nom" value={form.nom} onChange={handleChange} required />
        <input name="prenom" placeholder="Prénom" value={form.prenom} onChange={handleChange} required />
        <input name="poste" placeholder="Poste" value={form.poste} onChange={handleChange} />
        <input name="type_contrat" placeholder="Type de contrat" value={form.type_contrat} onChange={handleChange} />
        <input name="date_entree" type="date" placeholder="Date d'entrée" value={form.date_entree} onChange={handleChange} />
        <input name="date_sortie" type="date" placeholder="Date de sortie" value={form.date_sortie} onChange={handleChange} />
        <button type="submit">{editingId ? "Enregistrer" : "Ajouter"}</button>
        {editingId && <button type="button" onClick={handleCancel} style={{ marginLeft: 8 }}>Annuler</button>}
      </form>
      <table border="1" cellPadding={4} cellSpacing={0}>
        <thead>
          <tr>
            <th>Nom</th>
            <th>Prénom</th>
            <th>Poste</th>
            <th>Type de contrat</th>
            <th>Date d'entrée</th>
            <th>Date de sortie</th>
            <th>Actions</th>
          </tr>
        </thead>
        <tbody>
          {sortedAgents.map(a => (
            <tr key={a.id}>
              <td>{a.nom}</td>
              <td>{a.prenom}</td>
              <td>{a.poste}</td>
              <td>{a.type_contrat}</td>
              <td>{a.date_entree ? a.date_entree : ''}</td>
              <td>{a.date_sortie ? a.date_sortie : ''}</td>
              <td>
                <button onClick={() => handleEdit(a)}>Modifier</button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default Agents;
