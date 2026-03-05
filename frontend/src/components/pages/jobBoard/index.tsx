import { useAppSelector } from '../../../store/hooks';
import { useGetNearestJobPostsQuery } from '../../../store/features/jobPost/jobPostApi';
import { selectLocation } from '../../../store/features/user/userSelector';
import Header from './Header';
import Sidebar from './Sidebar';
import JobPostCard from '../../common/JobPostCard';
import JobBoardLayout from '../../layouts/JobBoardLayout';

const JobBoardPage = () => {
    const { lng, lat } = useAppSelector(selectLocation);
    const { data: jobPosts } = useGetNearestJobPostsQuery({ lng, lat }, { skip: !lng || !lat });

    return (
        <JobBoardLayout header={<Header />} sidebar={<Sidebar />}>
            <div className='lg:col-span-3 space-y-6'>
                <div>
                    <h2 className='text-2xl font-bold mb-6 flex items-center gap-3'>
                        Jobs Nearby
                        <span className='w-3 h-3 bg-yellow-400 rounded-full' />
                    </h2>
                    <div className='h-65 w-full flex flex-row items-center gap-4 overflow-x-auto'>
                        {jobPosts?.map((jobPost, idx) => (
                            <JobPostCard key={idx} jobPost={jobPost} />
                        ))}
                    </div>
                </div>
            </div>
        </JobBoardLayout>
    );
};

export default JobBoardPage;
