import React, { useEffect, useState } from "react";

function App() {
  const [cats, setCats] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch("/api/cats") // Make sure your Flask backend is running
      .then((res) => res.json())
      .then((data) => {
        setCats(data);
        setLoading(false);
      });
  }, []);

  return (
    <div style={{ padding: "2rem", fontFamily: "sans-serif" }}>
      <h1>🐱 Battle Cats Strategy Finder</h1>
      {loading ? (
        <p>Loading cat data...</p>
      ) : (
        <ul>
          {cats.map((cat, index) => (
            <li key={index}>
              <strong>{cat.name}</strong> — Trait: {cat.trait}
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}

export default App;
