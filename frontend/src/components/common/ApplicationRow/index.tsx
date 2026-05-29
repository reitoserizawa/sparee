import React from 'react';
import { format } from 'date-fns';
import { useNavigate } from 'react-router-dom';

import type { ApplicationRowProps } from './types';

import BriefCaseIcon from '../../../assets/icons/BriefCaseIcon';
import CalendarIcon from '../../../assets/icons/CalendarIcon';
import ClockIcon from '../../../assets/icons/ClockIcon';

import StatusBadge from '../StatusBadge';

const ApplicationRow: React.FC<ApplicationRowProps> = ({ app, index }) => {
    const navigate = useNavigate();

    return (
        <div
            className='group grid grid-cols-[1fr_auto] gap-4 items-center px-5 py-4 border-b border-gray-100 last:border-none hover:bg-gray-50/80 transition-colors cursor-pointer'
            style={{ animationDelay: `${index * 60}ms` }}
            onClick={() => navigate(`jobs/${app.job_post_id}`)}
        >
            {/* Left */}
            <div className='flex items-center gap-4 min-w-0'>
                {/* Icon */}
                <div className='w-9 h-9 rounded-lg bg-gray-100 flex items-center justify-center flex-shrink-0 group-hover:bg-gray-200 transition-colors'>
                    <BriefCaseIcon className='w-4 h-4 text-gray-500' />
                </div>

                {/* Info */}
                <div className='min-w-0'>
                    <p className='text-sm font-semibold text-gray-900 truncate group-hover:text-indigo-700 transition-colors'>
                        {app.job_post.title}
                    </p>
                    <div className='flex items-center gap-3 mt-0.5 flex-wrap'>
                        <span className='text-xs text-gray-400'>{'Department'}</span>
                        {app.job_post.address && (
                            <>
                                <span className='text-gray-300 text-xs'>·</span>
                                <span className='text-xs text-gray-400'>
                                    {app.job_post?.address?.full_address || 'N/A'}
                                </span>
                            </>
                        )}
                    </div>
                    <div className='flex items-center gap-3 mt-1.5 flex-wrap'>
                        <StatusBadge status={app.application_status} />
                        <span className='text-xs text-gray-400 flex items-center gap-1'>
                            <CalendarIcon className='w-3 h-3' />
                            {format(new Date(app.created_at), 'MMM d, yyyy')}
                        </span>
                        <span className='text-xs text-gray-400 flex items-center gap-1'>
                            <ClockIcon className='w-3 h-3' />
                            Updated {format(new Date(app.updated_at), 'MMM d')}
                        </span>
                    </div>
                </div>
            </div>

            {/* Right */}
            {/* <div className='flex items-center gap-2 flex-shrink-0'>
                <button
                    onClick={e => {
                        e.stopPropagation();
                        onEdit(app);
                    }}
                    className='px-3 py-1.5 rounded-lg text-xs font-medium border border-gray-200 text-gray-600 hover:border-gray-400 hover:text-gray-900 hover:bg-white transition-all bg-gray-50'
                    disabled={true}
                >
                    Edit Status
                </button>
                <ChevronRightIcon className='w-4 h-4 text-gray-300 group-hover:text-gray-500 transition-colors' />
            </div> */}
        </div>
    );
};

export default ApplicationRow;
