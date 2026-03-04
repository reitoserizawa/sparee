import { Navigate, Outlet } from 'react-router-dom';

import { useAppSelector } from '../store/hooks';
import { selectCurrentUser } from '../store/features/auth/authSelector';

const RequireAuth: React.ElementType = () => {
    const isAuthenticated = useAppSelector(selectCurrentUser);

    return isAuthenticated ? <Outlet /> : <Navigate to='/login' replace />;
};

export default RequireAuth;
