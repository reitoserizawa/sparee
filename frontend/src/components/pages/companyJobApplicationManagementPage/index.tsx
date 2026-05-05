import React from 'react';
import JobApplicantTable from '../../common/JobApplicantTable';

const CompanyJobApplicationManagementPage = (): React.ReactElement => {
    const jobPostTitle = 'Software Engineer'; // Placeholder, replace with actual job post title

    return (
        <div className='p-6 max-w-6xl mx-auto'>
            {/* Header */}
            <div className='flex justify-between items-center mb-6'>
                <div>
                    <h1 className='text-2xl font-semibold pb-3'>Job Applicants for {jobPostTitle}</h1>
                    <p className='text-gray-500 text-sm'>Manage your listings and applicants</p>
                </div>
            </div>

            {/* Table */}
            <JobApplicantTable />
        </div>
    );
};

export default CompanyJobApplicationManagementPage;
