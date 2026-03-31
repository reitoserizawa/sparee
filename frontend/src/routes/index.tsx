import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';
import LoginPage from '../components/pages/Login';
import RegisterPage from '../components/pages/Register';
import JobBoardPage from '../components/pages/jobBoard';
import PersistLogin from './PersistLogin';
import RequireAuth from './RequireAuth';
import RootLayout from '../components/layouts/RootLayout';
import JobPostDetailsPage from '../components/pages/jobPostDetails';
import JobApplicationsPage from '../components/pages/jobApplication';

const AppRoutes = () => {
    return (
        <BrowserRouter>
            <Routes>
                <Route element={<PersistLogin />}>
                    <Route path='/login' element={<LoginPage />} />
                    <Route path='/register' element={<RegisterPage />} />
                    <Route element={<RequireAuth />}>
                        <Route element={<RootLayout />}>
                            <Route path='/' element={<JobBoardPage />} />
                            <Route path='/job-posts/:jobPostId' element={<JobPostDetailsPage />} />
                            <Route path='/applications' element={<JobApplicationsPage />} />
                        </Route>
                    </Route>
                </Route>
                <Route path='*' element={<Navigate to='/' replace />} />
            </Routes>
        </BrowserRouter>
    );
};

export default AppRoutes;
