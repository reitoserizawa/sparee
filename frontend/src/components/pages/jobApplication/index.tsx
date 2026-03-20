import React, { useMemo } from 'react';

import { useGetUserJobApplicationsQuery } from '../../../store/features/jobApplication/jobApplicationApi';

import Card from '../../ui/Card';
import Sidebar from './Sidebar';
import JobPostDetailsLayout from '../../layouts/JobPostDetailsLayout';

const STATUS_COLORS: Record<string, string> = {
    applied: 'bg-blue-100 text-blue-600',
    reviewing: 'bg-yellow-100 text-yellow-600',
    accepted: 'bg-green-100 text-green-600',
    rejected: 'bg-red-100 text-red-600',
    withdrawn: 'bg-gray-100 text-gray-600',
};

const JobApplicationsPage: React.FC = () => {
    const { data: applications } = useGetUserJobApplicationsQuery(null);

    const stats = useMemo(() => {
        if (!applications) return {};

        return applications.reduce((acc: Record<string, number>, app) => {
            acc[app.application_status] = (acc[app.application_status] || 0) + 1;
            return acc;
        }, {});
    }, [applications]);

    if (!applications) return null;

    return (
        <JobPostDetailsLayout sidebar={<Sidebar stats={stats} />}>
            <div className='space-y-6'>
                {/* HEADER */}
                <div>
                    <h1 className='text-2xl font-semibold pb-3'>My Applications</h1>
                    <p className='text-gray-500 text-sm'>Track and manage all your job applications</p>
                </div>

                {/* STATS */}
                <div className='grid grid-cols-4 gap-4'>
                    {['applied', 'reviewing', 'accepted', 'rejected'].map(status => (
                        <Card key={status}>
                            <p className='text-sm text-gray-500 capitalize'>{status}</p>
                            <p className='text-2xl font-semibold'>{stats?.[status] || 0}</p>
                        </Card>
                    ))}
                </div>

                {/* APPLICATION LIST */}
                <Card>
                    <h2 className='font-semibold mb-4'>Recent Applications</h2>

                    <div className='space-y-4'>
                        {applications.map(app => {
                            const { application_status, job_post } = app;
                            const { title, description } = job_post;

                            return (
                                <div
                                    key={app.id}
                                    className='flex items-center justify-between border-b pb-4 last:border-none'
                                >
                                    <div>
                                        <h3 className='font-medium'>{title}</h3>
                                        {/* add company name */}
                                        <p className='text-sm text-gray-500'>{description}</p>
                                        <p className='text-xs text-gray-400 mt-1'>Applied on {app?.created_at}</p>
                                    </div>

                                    <div
                                        className={`px-3 py-1 rounded-full text-sm capitalize ${
                                            STATUS_COLORS[application_status]
                                        }`}
                                    >
                                        {application_status}
                                    </div>
                                </div>
                            );
                        })}
                    </div>
                </Card>
            </div>
        </JobPostDetailsLayout>
    );
};

export default JobApplicationsPage;
