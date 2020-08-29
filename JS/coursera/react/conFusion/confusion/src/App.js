import React from 'react';
import { Navbar, NavbarBrand } from 'reactstrap';
import Menu from './components/MenuComponent.js';
import './App.css';

function App() {
  return (
    <div>

        <Navbar dark color="primary">
            <div className="container">
                <NavbarBrand href="/">Ristorante ConFusion</NavbarBrand>
            </div>
        </Navbar>
        <Menu/>

    </div> // closing App
  );
}

export default App;
