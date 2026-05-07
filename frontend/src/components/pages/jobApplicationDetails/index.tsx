import React, { useState } from 'react';
import { format } from 'date-fns';
import { useNavigate, useParams } from 'react-router-dom';
import type {
    CompanyJobApplicationWithoutUser,
    JobApplicationStatus,
} from '../../../store/features/jobApplication/types';
import StatCard from '../../common/StatCard';
import ApplicationRow from '../../common/ApplicationRow';
import EditStatusModal from '../../common/EditStatusModal';
import ArrowLeftIcon from '../../../assets/icons/ArrowLeftIcon';
import BriefCaseIcon from '../../../assets/icons/BriefCaseIcon';
import MailIcon from '../../../assets/icons/MailIcon';
import CalendarIcon from '../../../assets/icons/CalendarIcon';
import AccountIcon from '../../../assets/icons/AccountIcon';
import FileIcon from '../../../assets/icons/FileIcon';
import CurrentApplicationCard from '../../common/CurrentApplicationCard';
import { useGetJobApplicationDetailsQuery } from '../../../store/features/jobApplication/jobApplicationApi';
import FullscreenLoader from '../../ui/Loader/FullScreenLoader';

const JobApplicationDetailsPage: React.FC = () => {
    const [modalOpen, setModalOpen] = useState(false);

    const navigate = useNavigate();
    const { companyId, jobPostId, applicationId } = useParams<{
        companyId: string;
        jobPostId: string;
        applicationId: string;
    }>();

    const { data: applicationDetails, isLoading: isApplicationDetailsLoading } = useGetJobApplicationDetailsQuery({
        companyId: Number(companyId),
        jobPostId: Number(jobPostId),
        jobApplicationId: Number(applicationId),
    });

    if (isApplicationDetailsLoading) {
        <FullscreenLoader withNavBar={true} />;
    }

    if (!applicationDetails) {
        return (
            <div className='min-h-screen flex items-center justify-center bg-gray-50'>
                <p className='text-gray-500'>Application not found.</p>
            </div>
        );
    }

    const openEdit = (app: CompanyJobApplicationWithoutUser) => {
        setModalOpen(true);
    };

    const closeEdit = () => {
        setModalOpen(false);
        setTimeout(() => null, 200);
    };

    const updateStatus = async (applicationId: number, newStatus: JobApplicationStatus) => {
        setTimeout(() => null, 200);
    };

    // Derived stats
    const statusCounts = applicationDetails?.history.reduce(
        (acc, a) => {
            acc[a.application_status] = (acc[a.application_status] ?? 0) + 1;
            return acc;
        },
        {} as Record<string, number>,
    );

    const { user } = applicationDetails;

    // TODO: add in db
    // const latestActivity =
    //     applications.length > 0
    //         ? format(
    //               new Date(
    //                   applications.reduce((latest, a) => (a.updated_at > latest.updated_at ? a : latest)).updated_at,
    //               ),
    //               'MMM d, yyyy',
    //           )
    //         : '—';

    return (
        <div className='min-h-screen bg-[#f8f8f7] font-sans'>
            {/* ── Top bar ── */}
            <div className='bg-white border-b border-gray-200 sticky top-0 z-30'>
                <div className='max-w-4xl mx-auto px-4 sm:px-6 h-14 flex items-center gap-3'>
                    <button
                        onClick={() => navigate(-1)}
                        className='flex items-center gap-1.5 text-sm text-gray-500 hover:text-gray-900 transition-colors'
                    >
                        <ArrowLeftIcon className='w-4 h-4' />
                        Back
                    </button>
                    <span className='text-gray-300'>/</span>
                    <span className='text-sm text-gray-400'>Applicants</span>
                    <span className='text-gray-300'>/</span>
                    <span className='text-sm font-medium text-gray-800 truncate max-w-[180px]'>{user.username}</span>
                </div>
            </div>

            <div className='max-w-4xl mx-auto px-4 sm:px-6 py-8 space-y-6'>
                {/* ── Profile card ── */}
                <div className='bg-white rounded-2xl border border-gray-200 overflow-hidden'>
                    {/* Colour accent */}
                    <div className='h-1.5 bg-gradient-to-r from-indigo-500 via-violet-500 to-purple-500' />

                    <div className='p-6 flex flex-col sm:flex-row sm:items-center gap-5'>
                        {/* Avatar */}
                        <div className='w-16 h-16 rounded-2xl bg-gradient-to-br from-indigo-100 to-violet-100 flex items-center justify-center flex-shrink-0'>
                            <span className='text-2xl font-bold text-indigo-600'>
                                {user.username
                                    .split(' ')
                                    .map(n => n[0])
                                    .join('')
                                    .slice(0, 2)}
                            </span>
                        </div>

                        {/* Info */}
                        <div className='flex-1 min-w-0'>
                            <h1 className='text-xl font-bold text-gray-900 leading-tight'>{user.username}</h1>
                            <div className='flex flex-wrap items-center gap-x-4 gap-y-1 mt-1.5'>
                                <span className='flex items-center gap-1.5 text-sm text-gray-500'>
                                    <AccountIcon className='w-3.5 h-3.5' />
                                    ID #{user.id}
                                </span>
                                <span className='flex items-center gap-1.5 text-sm text-gray-500'>
                                    <CalendarIcon className='w-3.5 h-3.5' />
                                    Joined {format(new Date(user.created_at), 'MMM yyyy')}
                                </span>
                            </div>
                        </div>

                        {/* Quick action */}
                        <a
                            href={`mailto:${user.email}`}
                            className='self-start sm:self-center inline-flex items-center gap-2 px-4 py-2 rounded-xl border border-gray-200 text-sm font-medium text-gray-700 hover:bg-gray-50 hover:border-gray-300 transition-all'
                        >
                            <MailIcon className='w-4 h-4' />
                            Send Message
                        </a>
                    </div>
                </div>

                <div className='flex items-center justify-between mb-3'>
                    <h2 className='text-sm font-semibold text-gray-900 flex items-center gap-2'>
                        <FileIcon className='w-4 h-4 text-gray-400' />
                        Selected Application
                    </h2>
                </div>
                {/* ── Current application ── */}
                <CurrentApplicationCard application={applicationDetails} onStatusChange={updateStatus} />

                <div className='flex items-center justify-between mb-3'>
                    <h2 className='text-sm font-semibold text-gray-900 flex items-center gap-2'>
                        <FileIcon className='w-4 h-4 text-gray-400' />
                        Application History
                    </h2>
                    <span className='text-xs text-gray-400'>
                        {applicationDetails.history.length} record{applicationDetails.history.length !== 1 ? 's' : ''}
                    </span>
                </div>

                {/* ── Stats row ── */}
                <div className='grid grid-cols-2 sm:grid-cols-4 gap-3'>
                    <StatCard label='Total' value={applicationDetails.history.length} sub='applications' />
                    <StatCard label='Reviewing' value={statusCounts['reviewing'] ?? 0} sub='in progress' />
                    <StatCard label='Rejected' value={statusCounts['rejected'] ?? 0} sub='closed' />
                    {/* TODO: add back after migration */}
                    {/* <StatCard label='Last Activity' value={latestActivity} /> */}
                </div>

                {/* ── Applications list ── */}
                <div>
                    <div className='bg-white rounded-2xl border border-gray-200 overflow-hidden'>
                        {applicationDetails.history.length === 0 ? (
                            <div className='py-16 flex flex-col items-center text-gray-400 gap-2'>
                                <BriefCaseIcon className='w-8 h-8 text-gray-300' />
                                <p className='text-sm'>No applications yet</p>
                            </div>
                        ) : (
                            applicationDetails.history.map((app, i) => (
                                <ApplicationRow key={app.id} app={app} index={i} onEdit={openEdit} />
                            ))
                        )}
                    </div>
                </div>
            </div>

            <EditStatusModal
                open={modalOpen}
                application={applicationDetails}
                onClose={closeEdit}
                onSave={updateStatus}
                isSaving={false}
            />
        </div>
    );
};

export default JobApplicationDetailsPage;
