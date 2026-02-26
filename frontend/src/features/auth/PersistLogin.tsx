import { useEffect } from 'react';
import { Outlet } from 'react-router-dom';

import { useRefreshMutation } from './authApi';
import { useAppSelector } from '../../apps/hooks';
import { selectCurrentUser } from './authSelector';

const PersistLogin: React.ElementType = () => {
    const isAuthenticated = useAppSelector(selectCurrentUser);
    const [refresh, { isLoading }] = useRefreshMutation();

    useEffect(() => {
        if (!isAuthenticated) {
            refresh(null);
        }
    }, [isAuthenticated, refresh]);

    if (isLoading) return <div>Loading...</div>;

    return <Outlet />;
};

export default PersistLogin;
