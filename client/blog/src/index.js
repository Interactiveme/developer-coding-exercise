import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import Home from './home/Home';
import Article from './post/Article'
import Header from './header/Header'
import reportWebVitals from './reportWebVitals';
import 'bootstrap/dist/css/bootstrap.css';
import { BrowserRouter, Route, Routes } from 'react-router-dom';

// Put any other imports below so that CSS from your
// components takes precedence over default styles.
ReactDOM.render(
  <React.StrictMode>
    <Header />
    <BrowserRouter>
        <Routes>
          <Route path="/" element={ <Home/>}></Route>
          <Route path="/post/:slug" element={<Article/>}></Route>
        </Routes>
      </BrowserRouter>
  </React.StrictMode>,
  document.getElementById('root')
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
