import React, { useState, useEffect } from 'react';
import './Membros.css';
import axios from 'axios';
import { getCLS, getFID, getLCP } from 'web-vitals';

const Membros = () => {
    const [membros, setMembros] = useState([]);

    useEffect(() => {
        axios.get('http://localhost:8000/api/membros/')
            .then(response => {
                setMembros(response.data);
            })
            .catch(error => {
                console.error('Houve um erro!', error);
            });
    }, []);

    return (
        <div>
            <h1>Cadastro de Mebros</h1>
            <ul>
                {membros.map(membro => (
                    <li key={membro.id}>{membro.nome}</li>
                ))}
            </ul>
        </div>
    );
}

export default Membros;