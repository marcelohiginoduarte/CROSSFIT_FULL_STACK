import React from 'react';
import { Link } from 'react-router-dom';
import './RightMenu.css';

const RightMenu = () => {
    return (
      <div className="menu">
        <h3>Menu</h3>
        <ul>
          <li>
            <Link to="/treinos">Treinos</Link>
          </li>
          <li>
            <Link to="/Mebros">Mebros</Link>
          </li>
          <li>
            <Link to="/plano-de-treinos">Plano de Treinos</Link>
          </li>
        </ul>
      </div>
    );
  };
  
  export default RightMenu;