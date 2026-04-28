import React from 'react';
import { useNavigate, useParams } from 'react-router-dom';
import { useGetJobPostsFromCompanyQuery } from '../../../store/features/jobPost/jobPostApi';

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
                        <th className='px-4 py-3 font-medium text-right'>Actions</th>
                    </tr>
                </thead>

                {/* Body */}
                <tbody>
                    {jobPosts.map(job => (
                        <tr
                            key={job.id}
                            className='border-t hover:bg-gray-50 cursor-pointer'
                            onClick={() => navigate(`/job-posts/${job.id}`)}
                        >
                            <td className='px-4 py-3 font-medium'>{job.title}</td>
                            <td className='px-4 py-3 text-gray-600'>
                                {job?.applications ? job.applications.length : 'N/A'}
                            </td>
                            <td className='px-4 py-3 text-gray-500'>{job.created_at}</td>
                            <td
                                className='px-4 py-3 text-right'
                                onClick={e => e.stopPropagation()} // prevent row click
                            >
                                <button
                                    className='text-sm text-blue-600 hover:underline'
                                    onClick={() => navigate(`/job-posts/${job.id}`)}
                                >
                                    View
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
