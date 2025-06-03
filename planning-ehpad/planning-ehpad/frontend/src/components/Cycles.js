import React, { useState, useEffect } from 'react';

function Cycles() {
  const [cycles, setCycles] = useState([]);
  const [form, setForm] = useState({ nom: '', structure_cycle: '' });

  useEffect(() => {
    fetch('http://localhost:5050/cycles')
      .then(res => res.json())
      .then(data => setCycles(data));
  }, []);

  const handleChange = e => setForm({ ...form, [e.target.name]: e.target.value });

  const handleSubmit = e => {
    e.preventDefault();
    fetch('http://localhost:5050/cycles', {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(form)
    })
      .then(res => res.json())
      .then(() => {
        setForm({ nom: '', structure_cycle: '' });
        fetch('http://localhost:5050/cycles')
          .then(res => res.json())
          .then(data => setCycles(data));
      });
  };

  return (
    <div>
      <h2>Cycles de travail</h2>
      <form onSubmit={handleSubmit}>
        <input name="nom" placeholder="Nom du cycle" value={form.nom} onChange={handleChange} required />
        <input name="structure_cycle" placeholder="Ex: 3T-2R-2T-3R" value={form.structure_cycle} onChange={handleChange} required />
        <button type="submit">Ajouter</button>
      </form>
      <ul>
        {cycles.map(c => (
          <li key={c.id}>{c.nom} — {c.structure_cycle}</li>
        ))}
      </ul>
    </div>
  );
}
export default Cycles;
