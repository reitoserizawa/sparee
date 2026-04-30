import React, { useState } from 'react';
import Button from '../../ui/Button';
import CompanyJobPostTable from '../../common/CompanyJobPostTable';
import CreateJobPostModal from '../../common/CreateJobPostModal';

const CompanyJobPostManagementPage = (): React.ReactElement => {
    const [isModalOpen, setIsModalOpen] = useState(false);

    return (
        <div className='p-6 max-w-6xl mx-auto'>
            {/* Header */}
            <div className='flex justify-between items-center mb-6'>
                <div>
                    <h1 className='text-2xl font-semibold pb-3'>Job Posts</h1>
                    <p className='text-gray-500 text-sm'>Manage your listings and applicants</p>
                </div>

                <Button
                    onClick={() => setIsModalOpen(true)}
                    className='px-4 py-2 rounded-full text-sm'
                    variant='secondary'
                >
                    + New Job Post
                </Button>
            </div>

            {/* Table */}
            <CompanyJobPostTable />

            {/* Modal */}
            {isModalOpen && <CreateJobPostModal onClose={() => setIsModalOpen(false)} />}
        </div>
    );
};

export default CompanyJobPostManagementPage;
