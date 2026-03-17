import React, { useState } from 'react';
import { useParams } from 'react-router-dom';

import { useGetJobPostDetailsQuery } from '../../../store/features/jobPost/jobPostApi';
import {
    useCreateJobApplicationsMutation,
    useDeleteJobApplicationMutation,
} from '../../../store/features/jobApplication/jobApplicationApi';

import CheckIcon from '../../../assets/icons/CheckIcon';
import Card from '../../ui/Card';
import Button from '../../ui/Button';
import DeleteModal from '../../common/DeleteModal';

const Sidebar: React.ElementType = () => {
    const { jobPostId } = useParams<{ jobPostId: string }>();
    const [isDeleteModalOpen, setIsDeleteModalOpen] = useState<boolean>(false);
    const [deleteJobApplication, { isLoading: deletingJobApplication }] = useDeleteJobApplicationMutation();

    const { data: jobPost } = useGetJobPostDetailsQuery({ jobPostId: Number(jobPostId) }, { skip: !jobPostId });
    const [createJobApplication] = useCreateJobApplicationsMutation();

    if (!jobPost) {
        return;
    }

    const { company, user_application: userApplication } = jobPost;
    const { name: companyName } = company;

    const handleApply = async () => {
        try {
            if (jobPostId) {
                await createJobApplication({ jobPostId: parseInt(jobPostId) }).unwrap();
            }
        } catch (err) {
            console.log(err);
        }
    };

    const handleDeleteApplication = async () => {
        if (userApplication) {
            await deleteJobApplication({ jobApplicationId: userApplication?.id }).unwrap();
            setIsDeleteModalOpen(false);
        }
    };

    // TODO: add case of "reviewing", "rejected", "accepted"

    const insertJobApplicationActionButton = (status: string | undefined) => {
        switch (status) {
            case 'applied':
                return (
                    <Button
                        variant='danger'
                        className='px-4 py-2 rounded-full text-sm'
                        onClick={() => setIsDeleteModalOpen(true)}
                    >
                        Delete Application
                    </Button>
                );
            case 'withdrawn':
                return (
                    <Button variant='primary' className='px-4 py-2 rounded-full text-sm'>
                        Reapply
                    </Button>
                );
            default:
                <Button variant='brand' onClick={() => handleApply()} className='w-full py-3 rounded-full'>
                    Apply now
                </Button>;
        }
    };

    return (
        <>
            {/* Apply Card */}
            <Card>
                <div
                    className={`flex items-center justify-center w-10 h-10 rounded-lg mb-4 ${
                        userApplication?.status === 'applied' ? 'bg-blue-100' : 'bg-green-100'
                    }`}
                >
                    <span
                        className={`material-symbols-outlined ${userApplication ? 'text-green-600' : 'text-blue-600'}`}
                    >
                        {userApplication?.status === 'applied' ? (
                            <CheckIcon size={24} color='blue' />
                        ) : (
                            <CheckIcon size={24} color='green' />
                        )}
                    </span>
                </div>

                <h3 className='font-semibold mb-2'>{userApplication ? 'Applied' : 'Apply now'}</h3>

                <p className='text-sm text-gray-500 mb-5'>
                    {userApplication
                        ? `You’ve applied to this position at ${companyName}.`
                        : `Please let ${companyName} know that you found this position.`}
                </p>

                {insertJobApplicationActionButton(userApplication?.status)}
            </Card>
            {/* Company Card */}
            <Card>
                <div className='w-10 h-10 bg-blue-600 rounded-lg flex items-center justify-center text-white mb-4'>
                    {companyName.slice(0, 1)}
                </div>
                <h3 className='font-semibold mb-2'>About {companyName}</h3>
                <p className='text-sm text-gray-500 mb-5'>
                    Faucibus ornare suspendisse sed nisi lacus sed. Volutpat ut venenatis tellus.
                </p>
                <Button variant='secondary' className='px-4 py-2 rounded-full text-sm'>
                    View company
                </Button>
            </Card>
            <DeleteModal
                open={isDeleteModalOpen}
                title='Delete Application'
                description='Are you sure you want to remove your job application?'
                loading={deletingJobApplication}
                onClose={() => setIsDeleteModalOpen(false)}
                onConfirm={handleDeleteApplication}
            />
        </>
    );
};

export default Sidebar;
