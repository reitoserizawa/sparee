import { useAppSelector } from '../../../store/hooks';
import { useGetNearestJobPostsQuery } from '../../../store/features/jobPost/jobPostApi';
import { selectLocation } from '../../../store/features/user/userSelector';
import Header from './Header';
import Sidebar from './Sidebar';
import JobPostCard from '../../common/JobPostCard';
import JobBoardLayout from '../../layouts/JobBoardLayout';
import FullscreenLoader from '../../common/Loader/FullScreenLoader';
import { useGetUserJobApplicationsQuery } from '../../../store/features/jobApplication/jobApplicationApi';
import EmptyJobState from '../../common/EmptyJobState';

const JobBoardPage = () => {
    const { lng, lat } = useAppSelector(selectLocation);
    const { data: nearestJobPosts, isLoading: loadingNearestJobPosts } = useGetNearestJobPostsQuery(
        { lng, lat },
        { skip: !lng || !lat },
    );
    const { data: userJobApplications, isLoading: loadingUserJobApplications } = useGetUserJobApplicationsQuery(null);

    const globalLoading = loadingUserJobApplications || loadingNearestJobPosts;

    if (globalLoading) return <FullscreenLoader />;

    return (
        <JobBoardLayout header={<Header />} sidebar={<Sidebar />}>
            <div className='lg:col-span-3 space-y-6'>
                <div>
                    <h2 className='text-2xl font-bold mb-6 flex items-center gap-3'>
                        Applied Jobs
                        <span className='w-3 h-3 bg-yellow-400 rounded-full' />
                    </h2>
                    <div className='h-65 w-full mb-6 flex flex-row items-center gap-4 overflow-x-auto'>
                        {userJobApplications && userJobApplications.length > 0 ? (
                            userJobApplications.map((jobApplication, idx) => (
                                <JobPostCard key={idx} jobPost={jobApplication.job_post} />
                            ))
                        ) : (
                            <EmptyJobState message="You haven't applied to any jobs yet" />
                        )}
                    </div>
                    <h2 className='text-2xl font-bold mb-6 flex items-center gap-3'>
                        Jobs Nearby
                        <span className='w-3 h-3 bg-yellow-400 rounded-full' />
                    </h2>
                    <div className='h-65 w-full mb-6 flex flex-row items-center gap-4 overflow-x-auto'>
                        {nearestJobPosts && nearestJobPosts.length > 0 ? (
                            nearestJobPosts.map((jobPost, idx) => <JobPostCard key={idx} jobPost={jobPost} />)
                        ) : (
                            <EmptyJobState message='No nearby jobs found' />
                        )}
                    </div>
                </div>
            </div>
        </JobBoardLayout>
    );
};

export default JobBoardPage;
