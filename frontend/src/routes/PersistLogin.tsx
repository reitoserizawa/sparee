import { useEffect, useState } from 'react';
import { Outlet } from 'react-router-dom';

import { useRefreshMutation } from '../store/features/auth/authApi';
import { useAppSelector } from '../store/hooks';
import { selectCurrentUser } from '../store/features/auth/authSelector';
import FullscreenLoader from '../components/ui/Loader/FullScreenLoader';

const PersistLogin: React.ElementType = () => {
    const isAuthenticated = useAppSelector(selectCurrentUser);
    const [refresh, { isLoading }] = useRefreshMutation();
    const [isChecking, setIsChecking] = useState(true);

    useEffect(() => {
        const verifyRefresh = async () => {
            try {
                if (!isAuthenticated) {
                    await refresh(null).unwrap();
                }
            } catch (err) {
                console.log(err);
            } finally {
                setIsChecking(false);
            }
        };

        verifyRefresh();
    }, [isAuthenticated, refresh]);

    if (isLoading || isChecking) {
        return <FullscreenLoader />;
    }

    return <Outlet />;
};

export default PersistLogin;
