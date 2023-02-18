import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import reportWebVitals from './reportWebVitals';
import {BrowserRouter as Router, Route, Routes} from "react-router-dom"
import Home from './pages/Home';
import { Login } from './pages/Login';
import {configureStore} from "@reduxjs/toolkit"
import { Provider } from 'react-redux';
import userReducer from "./features/redux/Users"
import { combineReducers } from '@reduxjs/toolkit';


const store  = configureStore({
  reducer: {
    user:userReducer,
  }
})
const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <Provider store={store}>
      <Router>
        <Routes>
          <Route  path='/' element={<Home />} />
          <Route  path='/login' element={<Login />} />
        </Routes>
    </Router>
    </Provider>
  </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
