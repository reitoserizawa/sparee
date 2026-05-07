import React from 'react';
import { format } from 'date-fns';
import { useNavigate, useParams } from 'react-router-dom';
import { useGetJobApplicationFromJobPostQuery } from '../../../store/features/jobApplication/jobApplicationApi';
import StatusBadge from '../StatusBadge';
import LinkIcon from '../../../assets/icons/LinkIcon';

const JobApplicationTable: React.FC = () => {
    const { companyId, jobPostId } = useParams();
    const { data: applicants = [] } = useGetJobApplicationFromJobPostQuery({
        companyId: Number(companyId),
        jobPostId: Number(jobPostId),
    });
    const navigate = useNavigate();

    return (
        <div className='bg-white border rounded-xl overflow-hidden'>
            <table className='w-full text-sm'>
                <thead className='bg-gray-50 text-left text-gray-600'>
                    <tr>
                        <th className='px-4 py-3 font-medium'>Applicant</th>
                        <th className='px-4 py-3 font-medium'>Email</th>
                        <th className='px-4 py-3 font-medium'>Status</th>
                        <th className='px-4 py-3 font-medium'>Created</th>
                        <th className='px-4 py-3 font-medium'>Updated</th>
                        <th className='px-4 py-3 font-medium text-right'>Details</th>
                    </tr>
                </thead>

                <tbody>
                    {applicants.map(applicant => (
                        <tr key={applicant.id} className='border-t hover:bg-gray-50 cursor-pointer'>
                            <td className='px-4 py-3'>
                                <div className='flex items-center gap-3'>{applicant.user.username}</div>
                            </td>
                            <td className='px-4 py-3 text-gray-600'>{applicant.user.email}</td>
                            <td className='px-4 py-3'>
                                <StatusBadge status={applicant.application_status} />
                            </td>
                            <td className='px-4 py-3 text-gray-500'>{format(new Date(applicant.created_at), 'PPP')}</td>
                            <td className='px-4 py-3 text-gray-500'>{format(new Date(applicant.updated_at), 'PPP')}</td>
                            <td className='px-4 py-3 text-right'>
                                <button
                                    className='text-sm text-blue-600 inline-flex items-center gap-1 group cursor-pointer'
                                    onClick={() =>
                                        navigate(
                                            `/companies/${companyId}/job-posts/${jobPostId}/applications/${applicant.id}`,
                                        )
                                    }
                                >
                                    <LinkIcon size={20} className='text-blue-600' />{' '}
                                    <span className='group-hover:underline'>View</span>
                                </button>
                            </td>
                        </tr>
                    ))}
                </tbody>
            </table>

            {applicants.length === 0 && <div className='p-6 text-center text-gray-500'>No applicants yet.</div>}
        </div>
    );
};

export default JobApplicationTable;
