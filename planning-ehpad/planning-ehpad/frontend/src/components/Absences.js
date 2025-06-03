import React, { useState, useEffect } from 'react';

function Absences() {
  const [absences, setAbsences] = useState([]);
  // Pour simplifier, pas de formulaire complet ici
  useEffect(() => {
    fetch('http://localhost:5050/absences')
      .then(res => res.json())
      .then(data => setAbsences(data));
  }, []);

  return (
    <div>
      <h2>Absences</h2>
      <ul>
        {absences.map(a => (
          <li key={a.id}>Agent {a.agent_id} : {a.date_debut} → {a.date_fin} ({a.motif})</li>
        ))}
      </ul>
    </div>
  );
}
export default Absences;
