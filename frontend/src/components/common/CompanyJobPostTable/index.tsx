import React from 'react';
import { format } from 'date-fns';
import { useNavigate, useParams } from 'react-router-dom';
import { useGetJobPostsFromCompanyQuery } from '../../../store/features/jobPost/jobPostApi';
import LinkIcon from '../../../assets/icons/LinkIcon';
import TableIcon from '../../../assets/icons/TableIcon';

const CompanyJobPostTable: React.FC = () => {
    const navigate = useNavigate();
    const { companyId } = useParams();
    const { data: jobPosts = [] } = useGetJobPostsFromCompanyQuery(Number(companyId));

    return (
        <div className='bg-white border rounded-xl overflow-hidden'>
            <table className='w-full text-sm'>
                {/* Header */}
                <thead className='bg-gray-50 text-left text-gray-600'>
                    <tr>
                        <th className='px-4 py-3 font-medium'>Title</th>
                        <th className='px-4 py-3 font-medium'>Applications</th>
                        <th className='px-4 py-3 font-medium'>Created</th>
                        <th className='px-4 py-3 font-medium text-right'>Details</th>
                        <th className='px-4 py-3 font-medium text-right'>Applications</th>
                    </tr>
                </thead>

                {/* Body */}
                <tbody>
                    {jobPosts.map(job => (
                        <tr key={job.id} className='border-t hover:bg-gray-50 cursor-pointer'>
                            <td className='px-4 py-3 font-medium'>{job.title}</td>
                            <td className='px-4 py-3 text-gray-600'>{job.application_count}</td>
                            <td className='px-4 py-3 text-gray-500'>{format(new Date(job.created_at), 'PPP')}</td>
                            <td className='px-4 py-3 text-right'>
                                <button
                                    className='text-sm text-blue-600 inline-flex items-center gap-1 group cursor-pointer'
                                    onClick={() => navigate(`/job-posts/${job.id}`)}
                                >
                                    <LinkIcon size={20} className='text-blue-600' />{' '}
                                    <span className='group-hover:underline'>View</span>
                                </button>
                            </td>
                            <td className='px-4 py-3 text-right'>
                                <button
                                    className='text-sm text-blue-600 inline-flex items-center gap-1 group cursor-pointer'
                                    onClick={() => navigate(`/companies/${companyId}/job-posts/${job.id}`)}
                                >
                                    <TableIcon size={20} className='text-blue-600' />{' '}
                                    <span className='group-hover:underline'>View</span>
                                </button>
                            </td>
                        </tr>
                    ))}
                </tbody>
            </table>

            {/* Empty state */}
            {jobPosts.length === 0 && (
                <div className='p-6 text-center text-gray-500'>No job posts yet. Create your first one.</div>
            )}
        </div>
    );
};

export default CompanyJobPostTable;
