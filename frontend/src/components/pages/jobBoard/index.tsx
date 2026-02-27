import { useAppSelector } from '../../../apps/hooks';
import { useGetNearestJobPostsQuery } from '../../../features/jobPost/jobPostApi';
import { selectLocation } from '../../../features/user/userSelector';

const JobBoardPage = () => {
    const { lng, lat } = useAppSelector(selectLocation);
    const { data } = useGetNearestJobPostsQuery({ lng, lat }, { skip: !lng || !lat });

    return (
        <div>
            {lng}
            {lat}
        </div>
    );
};

export default JobBoardPage;
