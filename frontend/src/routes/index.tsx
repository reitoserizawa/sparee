import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';
import Layout from '../components/layout';
import LoginPage from '../components/pages/Login';
import RegisterPage from '../components/pages/Register';
import DashboardPage from '../components/pages/Dashboard';
import PersistLogin from '../features/auth/PersistLogin';
import RequireAuth from '../features/auth/RequireAuth';
import JobBoardPage from '../components/pages/jobBoard';

const AppRoutes = () => {
    return (
        <BrowserRouter>
            <Routes>
                <Route element={<PersistLogin />}>
                    <Route path='/login' element={<LoginPage />} />
                    <Route path='/register' element={<RegisterPage />} />
                    <Route element={<RequireAuth />}>
                        <Route element={<Layout />}>
                            <Route path='/' element={<DashboardPage />} />
                            <Route path='/jobs' element={<JobBoardPage />} />
                        </Route>
                    </Route>
                </Route>
                <Route path='*' element={<Navigate to='/' replace />} />
            </Routes>
        </BrowserRouter>
    );
};

export default AppRoutes;
