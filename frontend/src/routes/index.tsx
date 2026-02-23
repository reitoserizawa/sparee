import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Layout from '../components/layout';
import LoginPage from '../components/pages/Login';
import SignUpPage from '../components/pages/SignUp';
import PublicRoute from './PublicRoute';
import PrivateRoute from './PrivateRoute';

const AppRoutes = () => {
    return (
        <BrowserRouter>
            <Routes>
                <Route element={<PublicRoute isAuthenticated={false} />}>
                    <Route path='/login' element={<LoginPage />} />
                    <Route path='/sign-up' element={<SignUpPage />} />
                </Route>
                <Route element={<PrivateRoute isAuthenticated={false} />}>
                    <Route element={<Layout />}>
                        <Route path='/' element={<div></div>} />
                    </Route>
                </Route>
            </Routes>
        </BrowserRouter>
    );
};

export default AppRoutes;
