import React from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Layout from './components/layout';
import LoginPage from './components/pages/Login';
import SignUpPage from './components/pages/SignUp';

const AppRouter = () => {
    return (
        <BrowserRouter>
            <Routes>
                <Route path='/login' element={<LoginPage />} />
                <Route path='/sign-up' element={<SignUpPage />} />
                <Route element={<Layout />}>
                    <Route path='/' element={<div></div>} />
                </Route>
            </Routes>
        </BrowserRouter>
    );
};

export default AppRouter;
