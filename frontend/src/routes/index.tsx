import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';
import LoginPage from '../components/pages/Login';
import RegisterPage from '../components/pages/Register';
import DashboardPage from '../components/pages/dashboard';
import PersistLogin from './PersistLogin';
import RequireAuth from './RequireAuth';
import JobBoardPage from '../components/pages/jobBoard';
import RootLayout from '../components/layouts/RootLayout';

const AppRoutes = () => {
    return (
        <BrowserRouter>
            <Routes>
                <Route element={<PersistLogin />}>
                    <Route path='/login' element={<LoginPage />} />
                    <Route path='/register' element={<RegisterPage />} />
                    <Route element={<RequireAuth />}>
                        <Route element={<RootLayout />}>
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
