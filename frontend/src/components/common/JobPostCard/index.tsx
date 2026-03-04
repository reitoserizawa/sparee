import React from 'react';
import type { CardProps } from './types';

const JobPostCard: React.FC<CardProps> = ({ jobPost }) => {
    const { title, company, skills, salary, location } = jobPost;

    return (
        <div className='h-60 w-80 rounded-2xl shrink-0  bg-gradient-to-br from-blue-500 to-cyan-500 p-6 shadow-xl text-white'>
            <div className='flex items-start gap-4'>
                <div className='flex h-12 w-12 items-center justify-center rounded-xl bg-white/20 backdrop-blur-sm'></div>

                <div className='flex-1'>
                    <h2 className='text-xl font-semibold leading-tight'>{title}</h2>
                    <p className='text-sm opacity-90'>{company?.name}</p>
                </div>
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

            <div className='mt-6 flex items-center justify-between text-sm font-medium'>
                <span>${salary}</span>
                <span className='opacity-90'>{location}</span>
            </div>
        </div>
    );
};

export default JobPostCard;
