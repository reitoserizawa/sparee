import type React from 'react';
import { Navigate, Outlet } from 'react-router-dom';

const PrivateRoute: React.FC<{ isAuthenticated: boolean }> = ({ isAuthenticated }) => {
    return isAuthenticated ? <Outlet /> : <Navigate to='/login' replace />;
};

export default PrivateRoute;
