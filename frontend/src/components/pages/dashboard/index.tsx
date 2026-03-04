import { useAppSelector } from '../../../store/hooks';
import { selectCurrentUser } from '../../../store/features/auth/authSelector';
import { useGetNearestJobPostsQuery } from '../../../store/features/jobPost/jobPostApi';
import { selectLocation } from '../../../store/features/user/userSelector';
import DashboardLayout from '../../layouts/DashboardLayout';
import Header from './Header';
import Sidebar from './Sidebar';

interface Job {
    title: string;
    salary: string;
    company: string;
}

const mockJobs: Job[] = [
    { title: 'UI Designer', salary: '$80k', company: 'Google' },
    { title: 'UX Designer', salary: '$90k', company: 'Meta' },
    { title: 'UI/UX Designer', salary: '$95k', company: 'Apple' },
    { title: 'Product Designer', salary: '$100k', company: 'Amazon' },
];

const locations = ['New York', 'Los Angeles', 'San Francisco'];

const DashboardPage = () => {
    const user = useAppSelector(selectCurrentUser);
    const { lng, lat } = useAppSelector(selectLocation);
    const { data: jobPosts } = useGetNearestJobPostsQuery({ lng, lat }, { skip: !lng || !lat });

    return (
        <DashboardLayout header={<Header />} sidebar={<Sidebar />}>
            <div className='lg:col-span-3 space-y-6'>
                {/* Featured Jobs */}
                <div>
                    <h2 className='text-2xl font-bold mb-6 flex items-center gap-3'>
                        Featured Jobs
                        <span className='w-3 h-3 bg-yellow-400 rounded-full' />
                    </h2>
                    <div className='grid grid-cols-1 md:grid-cols-2 gap-4'>
                        {mockJobs.map((job, idx) => (
                            <div
                                key={idx}
                                className='group bg-white/10 backdrop-blur-xl rounded-3xl p-6 hover:bg-white/20 transition-all duration-300 hover:scale-[1.02] border border-white/20 hover:border-white/40'
                            >
                                <div className='flex items-start justify-between mb-3'>
                                    <h3 className='font-bold text-xl'>{job.title}</h3>
                                    <div className='w-12 h-12 bg-gradient-to-br from-pink-500 to-purple-600 rounded-2xl flex-shrink-0 flex items-center justify-center group-hover:rotate-12 transition-transform' />
                                </div>
                                <div className='flex items-center gap-2 mb-4 opacity-90'>
                                    <div className='w-2 h-2 bg-green-400 rounded-full' />
                                    <span>Full-time</span>
                                </div>
                                <div className='flex items-center justify-between'>
                                    <span className='text-2xl font-bold text-green-400'>{job.salary}</span>
                                    <span className='text-indigo-100'>{job.company}</span>
                                </div>
                            </div>
                        ))}
                    </div>
                </div>
            </div>
        </DashboardLayout>
    );
};

export default DashboardPage;
