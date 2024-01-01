import React from 'react';
import AccessLogQuery from './AccessLogQuery';
import './App.css';

function App() {
  return (
    <div className="App" style={{ backgroundColor: 'orange', minHeight: '100vh', display: 'flex', flexDirection: 'column', alignItems: 'center' }}>
      <header className="App-header">
        <AccessLogQuery />
      </header>
    </div>
  );
}

export default App;
