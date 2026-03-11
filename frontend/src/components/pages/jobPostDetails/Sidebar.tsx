import React from 'react';
import { useParams } from 'react-router-dom';

import { useGetJobPostDetailsQuery } from '../../../store/features/jobPost/jobPostApi';

import CheckIcon from '../../../assets/icons/CheckIcon';
import Card from '../../ui/Card';

const Sidebar: React.ElementType = () => {
    const { jobPostId } = useParams<{ jobPostId: string }>();

    const { data: jobPost } = useGetJobPostDetailsQuery({ jobPostId: Number(jobPostId) }, { skip: !jobPostId });

    if (!jobPost) {
        return;
    }

    const { company } = jobPost;
    const { name: companyName } = company;

    return (
        <>
            {/* Apply Card */}
            <Card>
                <div className='flex items-center justify-center w-10 h-10 rounded-lg bg-blue-100 mb-4'>
                    <span className='material-symbols-outlined text-blue-600'>
                        <CheckIcon size={24} color='blue' />
                    </span>
                </div>
                <h3 className='font-semibold mb-2'>Apply now</h3>
                <p className='text-sm text-gray-500 mb-5'>
                    Please let {companyName} know that you found this position.
                </p>
                <button className='w-full bg-blue-600 text-white py-3 rounded-full font-medium'>Apply now</button>
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
                <button className='border px-4 py-2 rounded-full text-sm'>View company</button>
            </Card>
        </>
    );
};

export default Sidebar;
