import React from 'react';
import { format } from 'date-fns';
import { useParams } from 'react-router-dom';

import { useGetJobPostDetailsQuery } from '../../../store/features/jobPost/jobPostApi';
import convertSalaryType from '../../../utils/convertSalaryType';

import CheckIcon from '../../../assets/icons/CheckIcon';

const JobPostDetailsPage: React.ElementType = () => {
    const { jobPostId } = useParams<{ jobPostId: string }>();

    const { data: jobPost } = useGetJobPostDetailsQuery({ jobPostId: Number(jobPostId) }, { skip: !jobPostId });

    if (!jobPost) {
        return;
    }

    const {
        title,
        company,
        address,
        job_category,
        salary,
        salary_type: salaryType,
        description,
        created_at: createdAt,
    } = jobPost;
    const { full_address: city, state } = address;
    const { name: companyName } = company;

    return (
        <div className='bg-gray-50 min-h-[calc(100vh-61px)]'>
            <div className='max-w-6xl mx-auto px-6 py-8 flex gap-8'>
                {/* LEFT COLUMN */}
                <div className='flex-1'>
                    {/* Hero */}
                    <div className='bg-white rounded-2xl shadow-sm overflow-hidden'>
                        <div className='h-40 bg-gradient-to-r from-blue-900 to-blue-500' />

                        <div className='px-10 pb-10'>
                            {/* Logo */}
                            <div className='-mt-10 mb-4 flex justify-center'>
                                <div className='h-16 w-16 bg-blue-600 rounded-xl flex items-center justify-center text-white text-2xl font-bold'>
                                    {companyName.slice(0, 1)}
                                </div>
                            </div>

                            <h1 className='text-2xl font-semibold text-center mb-1'>{title}</h1>
                            <div className='flex flex-row justify-center gap-1'>
                                <h2 className='text-xl text-gray-500 leading-none mb-6'>{companyName}</h2>
                            </div>

                            {/* Meta Row */}
                            <div className='grid grid-cols-3 gap-6 text-sm text-gray-500 text-center border-b pb-6'>
                                <div>
                                    <span className='material-symbols-outlined block text-gray-400'>Location</span>
                                    <span>
                                        {city}, {state}
                                    </span>
                                </div>

                                <div>
                                    <span className='material-symbols-outlined block text-gray-400'>Category</span>
                                    <span>{job_category.name}</span>
                                </div>

                                <div>
                                    <span className='material-symbols-outlined block text-gray-400'>Salary</span>
                                    <span>
                                        ${salary} / {convertSalaryType(salaryType)}
                                    </span>
                                </div>
                            </div>

                            <div className='grid grid-cols-2 gap-6 text-sm text-gray-500 text-center border-b py-6'>
                                <div>
                                    <span className='material-symbols-outlined block text-gray-400'>Start</span>
                                    <span>{format(new Date(createdAt), 'PPP')}</span>
                                </div>

                                <div>
                                    <span className='material-symbols-outlined block text-gray-400'>End</span>
                                    <span>{format(new Date(createdAt), 'PPP')}</span>
                                </div>
                            </div>

                            {/* Description */}
                            <section className='mt-8'>
                                <div className='flex justify-between mb-3'>
                                    <h2 className='font-semibold text-lg'>Job Description</h2>
                                    <span className='text-sm text-gray-400'>
                                        Posted on: {format(new Date(createdAt), 'PPP')}
                                    </span>
                                </div>

                                <p className='text-gray-600 leading-relaxed'>{description}</p>
                            </section>

                            {/* Responsibilities */}
                            <section className='mt-8'>
                                <h2 className='font-semibold text-lg mb-3'>Responsibilities</h2>

                                <ul className='list-disc pl-6 text-gray-600 space-y-2'>
                                    <li>Neque sodales ut etiam sit amet nisl purus.</li>
                                    <li>Adipiscing elit ut aliquam purus sit amet.</li>
                                    <li>Mauris commodo quis imperdiet massa tincidunt.</li>
                                </ul>
                            </section>

                            {/* Requirements */}
                            <section className='mt-8'>
                                <h2 className='font-semibold text-lg mb-3'>Job Requirements</h2>

                                <ul className='list-disc pl-6 text-gray-600 space-y-2'>
                                    <li>Neque sodales ut etiam sit amet nisl purus.</li>
                                    <li>Adipiscing elit ut aliquam purus sit amet.</li>
                                    <li>Mauris commodo quis imperdiet massa tincidunt.</li>
                                </ul>
                            </section>
                        </div>
                    </div>
                </div>

                {/* RIGHT SIDEBAR */}
                <aside className='w-80 space-y-6'>
                    {/* Apply Card */}
                    <div className='bg-white rounded-2xl p-6 shadow-sm'>
                        <div className='flex items-center justify-center w-10 h-10 rounded-lg bg-blue-100 mb-4'>
                            <span className='material-symbols-outlined text-blue-600'>
                                <CheckIcon size={24} color='blue' />
                            </span>
                        </div>

                        <h3 className='font-semibold mb-2'>Apply now</h3>

                        <p className='text-sm text-gray-500 mb-5'>
                            Please let {companyName} know that you found this position.
                        </p>

                        <button className='w-full bg-blue-600 text-white py-3 rounded-full font-medium'>
                            Apply now
                        </button>
                    </div>

                    {/* Company Card */}
                    <div className='bg-white rounded-2xl p-6 shadow-sm'>
                        <div className='w-10 h-10 bg-blue-600 rounded-lg flex items-center justify-center text-white mb-4'>
                            {companyName.slice(0, 1)}
                        </div>

                        <h3 className='font-semibold mb-2'>About {companyName}</h3>

                        <p className='text-sm text-gray-500 mb-5'>
                            Faucibus ornare suspendisse sed nisi lacus sed. Volutpat ut venenatis tellus.
                        </p>

                        <button className='border px-4 py-2 rounded-full text-sm'>View company</button>
                    </div>
                </aside>
            </div>
        </div>
    );
};

export default JobPostDetailsPage;
