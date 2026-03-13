import React from 'react';
import { useParams } from 'react-router-dom';

import { useGetJobPostDetailsQuery } from '../../../store/features/jobPost/jobPostApi';
import { useCreateJobApplicationsMutation } from '../../../store/features/jobApplication/jobApplicationApi';

import CheckIcon from '../../../assets/icons/CheckIcon';
import Card from '../../ui/Card';
import Button from '../../ui/Button';

const Sidebar: React.ElementType = () => {
    const { jobPostId } = useParams<{ jobPostId: string }>();

    const { data: jobPost } = useGetJobPostDetailsQuery({ jobPostId: Number(jobPostId) }, { skip: !jobPostId });
    const [createJobApplication] = useCreateJobApplicationsMutation();

    if (!jobPost) {
        return;
    }

    const { company, application_status } = jobPost;
    const { name: companyName } = company;
    const hasApplied = application_status;

    const handleApply = async () => {
        try {
            if (jobPostId) {
                await createJobApplication({ jobPostId: parseInt(jobPostId) }).unwrap();
            }
        } catch (err) {
            console.log(err);
        }
    };

    return (
        <>
            {/* Apply Card */}
            <Card>
                <div
                    className={`flex items-center justify-center w-10 h-10 rounded-lg mb-4 ${
                        hasApplied ? 'bg-green-100' : 'bg-blue-100'
                    }`}
                >
                    <span className={`material-symbols-outlined ${hasApplied ? 'text-green-600' : 'text-blue-600'}`}>
                        {hasApplied ? <CheckIcon size={24} color='green' /> : <CheckIcon size={24} color='blue' />}
                    </span>
                </div>

                <h3 className='font-semibold mb-2'>{hasApplied ? 'Applied' : 'Apply now'}</h3>

                <p className='text-sm text-gray-500 mb-5'>
                    {hasApplied
                        ? `You’ve applied to this position at ${companyName}.`
                        : `Please let ${companyName} know that you found this position.`}
                </p>

                {!hasApplied && (
                    <Button variant='brand' onClick={() => handleApply()} className='w-full py-3 rounded-full'>
                        Apply now
                    </Button>
                )}
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
        </>
    );
};

export default Sidebar;
