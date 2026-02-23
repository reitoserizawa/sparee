import type React from 'react';
import { Navigate, Outlet } from 'react-router-dom';

const PublicRoute: React.FC<{ isAuthenticated: boolean }> = ({ isAuthenticated }) => {
    return !isAuthenticated ? <Outlet /> : <Navigate to='/dashboard' replace />;
};

export default PublicRoute;
