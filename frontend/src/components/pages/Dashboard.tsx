import { useAppSelector } from '../../apps/hooks';
import { selectAuth } from '../../features/auth/authSelector';

const DashboardPage = () => {
    const user = useAppSelector(selectAuth);

    return <div>{user?.username}</div>;
};

export default DashboardPage;
