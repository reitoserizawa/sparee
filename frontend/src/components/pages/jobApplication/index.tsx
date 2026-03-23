import React, { useMemo } from 'react';

import { useGetUserJobApplicationsQuery } from '../../../store/features/jobApplication/jobApplicationApi';

import Card from '../../ui/Card';
import Sidebar from './Sidebar';
import JobPostDetailsLayout from '../../layouts/JobPostDetailsLayout';
import FullscreenLoader from '../../ui/Loader/FullScreenLoader';
import JobApplicationListItem from '../../common/JobApplicationListItem';

const JobApplicationsPage: React.FC = () => {
    const { data: jobApplications, isLoading: loadingApplications } = useGetUserJobApplicationsQuery(null);
    const isGlobalLoading = loadingApplications;

    const stats = useMemo(() => {
        if (!jobApplications) return {};

        return jobApplications.reduce((acc: Record<string, number>, app) => {
            acc[app.application_status] = (acc[app.application_status] || 0) + 1;
            return acc;
        }, {});
    }, [jobApplications]);

    if (!jobApplications) return null;
    if (isGlobalLoading) return <FullscreenLoader withNavBar={true} />;

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
                <Card>
                    <h2 className='font-semibold mb-4'>Recent Applications</h2>

                    <div className='space-y-4'>
                        {jobApplications.map(jobApplication => (
                            <JobApplicationListItem key={jobApplication.id} jobApplication={jobApplication} />
                        ))}
                    </div>
                </Card>
            </div>
        </JobPostDetailsLayout>
    );
};

export default JobApplicationsPage;
