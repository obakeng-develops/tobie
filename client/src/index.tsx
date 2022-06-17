import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import {
  BrowserRouter,
  Routes,
  Route
} from "react-router-dom";
import Dashboard from './pages/Dashboard';
import Popup from './pages/Popup';
import SignIn from './pages/SignIn';

const root = ReactDOM.createRoot(
  document.getElementById('root') as HTMLElement
);
root.render(
  <BrowserRouter>
    <Routes>
      <Route path="/" element={<App />}/>
      <Route path="/popup" element={<Popup/>}/>
      <Route path="/signin" element={<SignIn/>}/>
    </Routes>
  </BrowserRouter>
);

