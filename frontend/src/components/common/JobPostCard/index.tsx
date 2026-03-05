import React from 'react';
import type { CardProps } from './types';

import EnterpriseIcon from '../../../assets/icons/EnterpriseIcon';
import convertSalaryType from '../../../utils/convertSalaryType';

const JobPostCard: React.FC<CardProps> = ({ jobPost }) => {
    const { title, company, address, skills, salary, salary_type: salaryType } = jobPost;
    const { name: companyName } = company;

    return (
        <div className='h-60 w-90 rounded-2xl shrink-0  bg-gradient-to-br from-blue-500 to-cyan-500 p-6 text-white transform hover:-translate-y-1 transition-all duration-200'>
            <div className='flex items-start gap-4'>
                <div className='flex h-12 w-12 items-center justify-center rounded-xl bg-white/20 backdrop-blur-sm'>
                    <EnterpriseIcon size={24} color='white' />
                </div>

                <div className='flex-1'>
                    <h2 className='text-xl font-semibold leading-tight'>{title}</h2>
                    <p className='text-sm opacity-90'>{companyName}</p>
                </div>
            </div>

            <div className='mt-4 flex flex-wrap gap-2'>
                <p className='text-sm opacity-90'>&#x1F4CC; {address?.full_address}</p>
            </div>

            <div className='mt-4 flex flex-wrap gap-2'>
                {skills?.map((skill, index) => (
                    <span
                        key={index}
                        className='rounded-full bg-white/20 px-3 py-1 text-xs font-medium backdrop-blur-sm'
                    >
                        {skill}
                    </span>
                ))}
            </div>

            <div className='mt-4 flex-shrink-0'>
                <span className='pt-2 text-4xl font-bold uppercase'>${salary} </span>
                <span className=''>/ {convertSalaryType(salaryType)}</span>
            </div>
        </div>
    );
};

export default JobPostCard;
