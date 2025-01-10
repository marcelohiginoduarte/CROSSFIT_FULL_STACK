import './App.css';
import React from 'react';
import Membros from './components/Membros';
import RightMenu from './routes';
import SidebarBox from './components/Sidebar';

function App() {
  return (
    <div className="App">
      <Membros />
      <SidebarBox />
    </div>
  );
}

export default App;
