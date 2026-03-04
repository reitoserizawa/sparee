import { useAppSelector } from '../../../store/hooks';
import { useGetNearestJobPostsQuery } from '../../../store/features/jobPost/jobPostApi';
import { selectLocation } from '../../../store/features/user/userSelector';
import Card from '../../common/Card';

const JobBoardPage = () => {
    const { lng, lat } = useAppSelector(selectLocation);
    const { data: jobPosts } = useGetNearestJobPostsQuery({ lng, lat }, { skip: !lng || !lat });

    return (
        <div>
            {jobPosts?.map((jobPost, idx) => (
                <Card
                    key={idx}
                    title={jobPost.title}
                    description={jobPost.description}
                    salary={jobPost.salary}
                    skills={['Test']}
                />
            ))}
        </div>
    );
};

export default JobBoardPage;
