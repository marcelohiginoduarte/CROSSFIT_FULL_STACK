import React, { useState } from "react";
import "./sidebar.css";

function SidebarBox() {
  // Estado para controlar o submenu
    const [showMembrosOptions, setShowMembrosOptions] = useState(false);
    const [showTreinosOptions, setShowTreinosOptions] = useState(false);
    const [sowTipoplanoOptions, setShowTipoplanoOptions] = useState(false);

  // Função para alternar a exibição do submenu
    const toggleMembrosOptions = () => {setShowMembrosOptions(!showMembrosOptions);};
    const toggleTreinosOptions = () => {setShowTreinosOptions(!showTreinosOptions);};
    const toggleTipoPLanoOptions = () =>  {setShowTipoplanoOptions(!sowTipoplanoOptions);};
        
    

    return (
        <div className="app">
          <div className="sidebar">
            <div className="apresentacao">
              <h1>Bem vindo a sua BOX!</h1>
            </div>
    
            <div className="menu">
              <h2>Menu</h2>
              <ul>
                <li onClick={toggleMembrosOptions} style={{ cursor: "pointer" }}>
                  Membros
                </li>
                {showMembrosOptions && (
                  <ul className="submenu">
                    <li>Criar Membros</li>
                    <li>Ver Membros</li>
                  </ul>
                )}
    
                <li onClick={toggleTreinosOptions} style={{ cursor: "pointer" }}>
                  Treinos
                </li>
                {showTreinosOptions && (
                  <ul className="submenu">
                    <li>Criar Treinos</li>
                    <li>Ver Treinos</li>
                  </ul>
                )}
                <li onClick={toggleTipoPLanoOptions} style={{ cursor: "pointer" }}>
                    Tipo de Planos</li>
                {sowTipoplanoOptions &&(
                     <ul className="submenu">
                    <li>Criar Plano</li>
                    <li>Ver Planos</li>
                    </ul>
                )}
                </ul>
            </div>
          </div>
        </div>
      );
}    

export default SidebarBox;
