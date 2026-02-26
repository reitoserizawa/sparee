import type React from 'react';
import { Navigate, Outlet } from 'react-router-dom';
import { useAppSelector } from '../apps/hooks';
import { selectCurrentUser } from '../features/auth/authSelector';

const PublicRoute: React.ElementType = () => {
    const isAuthenticated = useAppSelector(selectCurrentUser);
    return !isAuthenticated ? <Outlet /> : <Navigate to='/dashboard' replace />;
};

export default PublicRoute;
