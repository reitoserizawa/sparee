import { useAppSelector } from '../../apps/hooks';
import { selectLocation } from '../../features/user/userSelector';

const JobBoardPage = () => {
    const { lng, lat } = useAppSelector(selectLocation);

    return (
        <div>
            {lng}
            {lat}
        </div>
    );
};

export default JobBoardPage;
