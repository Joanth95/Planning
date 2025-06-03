import React from 'react';
import { BrowserRouter as Router, Route, Routes, Link } from 'react-router-dom';
import Agents from './components/Agents';
import Cycles from './components/Cycles';
import Horaires from './components/Horaires';
import Absences from './components/Absences';

function App() {
  return (
    <Router>
      <div style={{ padding: 16 }}>
        <h1>Planning EHPAD</h1>
        <nav>
          <Link to="/">Agents</Link> | <Link to="/cycles">Cycles</Link> | <Link to="/horaires">Horaires</Link> | <Link to="/absences">Absences</Link>
        </nav>
        <Routes>
          <Route path="/" element={<Agents />} />
          <Route path="/cycles" element={<Cycles />} />
          <Route path="/horaires" element={<Horaires />} />
          <Route path="/absences" element={<Absences />} />
        </Routes>
      </div>
    </Router>
  );
}
export default App;
