import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Layout from '../components/layout';
import LoginPage from '../components/pages/Login';
import PublicRoute from './PublicRoute';
import PrivateRoute from './PrivateRoute';
import RegisterPage from '../components/pages/Register';
import DashboardPage from '../components/pages/Dashboard';

const AppRoutes = () => {
    return (
        <BrowserRouter>
            <Routes>
                <Route element={<PublicRoute />}>
                    <Route path='/login' element={<LoginPage />} />
                    <Route path='/register' element={<RegisterPage />} />
                </Route>
                <Route element={<PrivateRoute />}>
                    <Route element={<Layout />}>
                        <Route path='/' element={<DashboardPage />} />
                    </Route>
                </Route>
            </Routes>
        </BrowserRouter>
    );
};

export default AppRoutes;
