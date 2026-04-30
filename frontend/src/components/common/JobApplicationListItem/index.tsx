import React from 'react';
import { format } from 'date-fns';
import type { JobApplication } from '../../../store/features/jobApplication/types';
import { STATUS_COLORS } from '../../../constants/STATUS_COLORS';

interface JobApplicationListItemProps {
    jobApplication: JobApplication;
}

const JobApplicationListItem: React.FC<JobApplicationListItemProps> = ({ jobApplication }) => {
    const {
        application_status: applicationStatus,
        created_at: createdAt,
        updated_at: updatedAt,
        job_post: jobPost,
    } = jobApplication;
    const { title, description } = jobPost;

    return (
        <div className='flex items-center justify-between border-b pb-4 last:border-none'>
            <div>
                <h3 className='font-medium'>{title}</h3>
                {/* TODO: add company name */}
                <p className='text-sm text-gray-500'>{description}</p>
                <p className='text-xs text-gray-400 mt-1'>Applied on {format(new Date(createdAt), 'PPP')}</p>
                {applicationStatus != 'applied' && updatedAt && (
                    <p className='text-xs text-gray-400 mt-1'>Updated on {format(new Date(updatedAt), 'PPP')}</p>
                )}
            </div>

            <div className={`px-3 py-1 rounded-full text-sm capitalize ${STATUS_COLORS[applicationStatus]}`}>
                {applicationStatus}
            </div>
        </div>
    );
};

export default JobApplicationListItem;
