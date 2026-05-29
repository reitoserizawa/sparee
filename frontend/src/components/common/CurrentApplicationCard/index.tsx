import React, { useState } from 'react';
import type { CurrentApplicationCardProps } from './types';
import type { JobApplicationStatus } from '../../../store/features/jobApplication/types';
import { STATUS_CONFIG } from '../../../constants/STATUS_COLORS';
import BriefCaseIcon from '../../../assets/icons/BriefCaseIcon';
import CalendarIcon from '../../../assets/icons/CalendarIcon';
import ClockIcon from '../../../assets/icons/ClockIcon';
import { format } from 'date-fns';
import BuildingIcon from '../../../assets/icons/BuildingIcon';
import StatusDropdown from '../StatusDropdown/Index';
import CheckIcon from '../../../assets/icons/CheckIcon';
import { useChangeJobApplicationStatusMutation } from '../../../store/features/jobApplication/jobApplicationApi';
import { isErrorWithMessage } from '../../../store/features/base/helpers';
import Error from '../../ui/Error';
import { useParams } from 'react-router-dom';

const CurrentApplicationCard: React.FC<CurrentApplicationCardProps> = ({ application }) => {
    const { companyId } = useParams<{
        companyId: string;
        jobPostId: string;
        applicationId: string;
    }>();

    const [status, setStatus] = useState<JobApplicationStatus>(application.application_status);
    const [justSaved, setJustSaved] = useState(false);
    const [changeStatus, { isLoading: isSaving, isError, error }] = useChangeJobApplicationStatusMutation();

    const cfg = STATUS_CONFIG[status]; // now reactive to changes

    const handleStatusChange = async (newStatus: JobApplicationStatus) => {
        if (!companyId || newStatus === status || isSaving) return;
        const previous = status;
        setStatus(newStatus);
        try {
            await changeStatus({
                companyId: parseInt(companyId),
                jobPostId: application.job_post.id,
                jobApplicationId: application.id,
                newStatus,
            }).unwrap();
            setJustSaved(true);
            setTimeout(() => setJustSaved(false), 2000);
        } catch (e) {
            console.log('error', e);
            setStatus(previous); // rollback on failure
        }
    };

    return (
        <div
            className={`relative bg-white rounded-2xl border-2 ${cfg.border} shadow-lg ${cfg.glow} transition-all duration-300`}
        >
            <div className='px-5 pt-5 pb-5'>
                {/* Job title + meta */}
                <div className='flex items-start gap-4'>
                    <div className='w-11 h-11 rounded-xl bg-gray-100 flex items-center justify-center flex-shrink-0'>
                        <BriefCaseIcon className='w-5 h-5 text-gray-500' />
                    </div>

                    <div className='flex-1 min-w-0 pt-0.5'>
                        <h2 className='text-base font-bold text-gray-900 leading-snug truncate pr-28'>
                            {application.job_post.title}
                        </h2>
                        <div className='flex flex-wrap items-center gap-x-3 gap-y-1 mt-1'>
                            {application.job_post.address && (
                                <span className='flex items-center gap-1 text-xs text-gray-500'>
                                    <BuildingIcon className='w-3 h-3' />
                                    {application.job_post.address.full_address || 'N/A'}
                                </span>
                            )}
                        </div>
                    </div>
                </div>

                {/* Divider */}
                <div className='border-t border-gray-100 my-4' />

                {/* Status row + timestamps */}
                <div className='flex flex-wrap items-center justify-between gap-3'>
                    {/* Left: status control + saved indicator */}
                    <div className='flex items-center gap-2.5'>
                        <span className='text-xs font-medium text-gray-400'>Status</span>
                        <StatusDropdown current={status} onChange={handleStatusChange} isSaving={isSaving} />
                        {justSaved && (
                            <span className='flex items-center gap-1 text-xs text-emerald-600 font-medium animate-pulse'>
                                <CheckIcon className='w-3.5 h-3.5' />
                                Saved
                            </span>
                        )}
                        {isError && isErrorWithMessage(error) && <Error message={error?.data?.message} />}
                    </div>

                    {/* Right: timestamps */}
                    <div className='flex items-center gap-4'>
                        <span className='flex items-center gap-1.5 text-xs text-gray-400'>
                            <CalendarIcon className='w-3 h-3' />
                            Applied {format(new Date(application.created_at), 'MMM d, yyyy')}
                        </span>
                        <span className='flex items-center gap-1.5 text-xs text-gray-400'>
                            <ClockIcon className='w-3 h-3' />
                            Updated {format(new Date(application.updated_at), 'MMM d, yyyy')}
                        </span>
                    </div>
                </div>
            </div>
        </div>
    );
};

export default CurrentApplicationCard;
