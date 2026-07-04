import React, { useState } from "react";
import "./App.css";

// TypeScript-Definition für unsere Tabs
interface Tab {
  id: string;
  label: string;
}

export default function App() {
  // state für den aktuellen aktiven Tab (Standard: "Dashboard")
  const [activeTab, setActiveTab] = useState<string>("Dashboard");

  // Funktion, die den passenden Inhalt für das Hauptfenster liefert
  const renderContent = () => {
    switch (activeTab) {
      case "Dashboard":
        return (
          <>
            <h2>Dashboard</h2>
            <div className="grid">
              <div className="card"><h3>CPU</h3><p>0 %</p></div>
              <div className="card"><h3>GPU</h3><p>0 %</p></div>
              <div className="card"><h3>RAM</h3><p>0 GB</p></div>
              <div className="card"><h3>FPS</h3><p>0</p></div>
            </div>
          </>
        );
      case "Games":
        return (
          <>
            <h2>🎮 Games Launcher</h2>
            <p style={{ color: "#a0a5b5", marginTop: "15px" }}>Hier listen wir bald deine installierten Spiele auf.</p>
          </>
        );
      case "Performance":
        return (
          <>
            <h2>📊 Performance Details</h2>
            <p style={{ color: "#a0a5b5", marginTop: "15px" }}>Detaillierte Graphen für CPU, GPU und RAM Auslastung.</p>
          </>
        );
      case "AI":
        return (
          <>
            <h2>🤖 Nexus AI</h2>
            <p style={{ color: "#a0a5b5", marginTop: "15px" }}>Das Interface für deinen persönlichen Sprach- und Textassistenten.</p>
          </>
        );
      default:
        return (
          <>
            <h2>{activeTab}</h2>
            <p style={{ color: "#a0a5b5", marginTop: "15px" }}>Dieser Bereich befindet sich noch im Aufbau...</p>
          </>
        );
    }
  };

  // Liste aller verfügbaren Tabs
  const tabs: Tab[] = [
    { id: "Dashboard", label: "🏠 Dashboard" },
    { id: "Games", label: "🎮 Games" },
    { id: "Performance", label: "📊 Performance" },
    { id: "AI", label: "🤖 AI" },
    { id: "Music", label: "🎵 Music" },
    { id: "Notes", label: "📝 Notes" },
    { id: "Calendar", label: "📅 Calendar" },
    { id: "Settings", label: "⚙️ Settings" },
  ];

  return (
    <div className="app">
      <aside className="sidebar">
        <h1 className="logo">NEXUS</h1>

        <nav>
          {tabs.map((tab) => (
            <button
              key={tab.id}
              // Wenn die ID mit dem State übereinstimmt, zieht dein CSS die Klasse '.active'
              className={activeTab === tab.id ? "active" : ""}
              onClick={() => setActiveTab(tab.id)}
            >
              {tab.label}
            </button>
          ))}
        </nav>
      </aside>

      <main className="main">
        {/* Hier wird der Inhalt dynamisch gerendert */}
        {renderContent()}
      </main>
    </div>
  );
}