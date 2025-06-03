import React, { useState, useEffect } from 'react';

function Horaires() {
  const [horaires, setHoraires] = useState([]);
  const [form, setForm] = useState({ nom: '', code: '', heure_debut: '', heure_fin: '', pause: '' });

  useEffect(() => {
    fetch('http://localhost:5050/horaires')
      .then(res => res.json())
      .then(data => setHoraires(data));
  }, []);

  const handleChange = e => setForm({ ...form, [e.target.name]: e.target.value });

  const handleSubmit = e => {
    e.preventDefault();
    fetch('http://localhost:5050/horaires', {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(form)
    })
      .then(res => res.json())
      .then(() => {
        setForm({ nom: '', code: '', heure_debut: '', heure_fin: '', pause: '' });
        fetch('http://localhost:5050/horaires')
          .then(res => res.json())
          .then(data => setHoraires(data));
      });
  };

  return (
    <div>
      <h2>Horaires</h2>
      <form onSubmit={handleSubmit}>
        <input name="nom" placeholder="Nom" value={form.nom} onChange={handleChange} />
        <input name="code" placeholder="Code" value={form.code} onChange={handleChange} />
        <input name="heure_debut" placeholder="Début (ex: 07:00)" value={form.heure_debut} onChange={handleChange} />
        <input name="heure_fin" placeholder="Fin (ex: 19:00)" value={form.heure_fin} onChange={handleChange} />
        <input name="pause" placeholder="Pause (h)" value={form.pause} onChange={handleChange} />
        <button type="submit">Ajouter</button>
      </form>
      <ul>
        {horaires.map(h => (
          <li key={h.id}>{h.nom} ({h.code}) : {h.heure_debut} - {h.heure_fin} (pause {h.pause}h)</li>
        ))}
      </ul>
    </div>
  );
}
export default Horaires;
