import React from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Layout from './components/Layout';

const AppRouter = () => {
  return (
    <BrowserRouter>
      <Routes>
        <Route element={<Layout />}>
          <Route path='/' element={<div>Home</div>} />
        </Route>
      </Routes>
    </BrowserRouter>
  );
};

export default AppRouter;
