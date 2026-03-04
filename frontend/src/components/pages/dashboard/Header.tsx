import React from 'react';
import { useAppSelector } from '../../../store/hooks';
import { selectCurrentUser } from '../../../store/features/auth/authSelector';

const Header: React.ElementType = () => {
    const user = useAppSelector(selectCurrentUser);

    return (
        <>
            <div className='flex items-center gap-4'>
                <div>
                    <p className='text-sm text-gray-500'>Welcome back, {user}!</p>
                    <h1 className='text-3xl font-bold'>Discover Jobs &#128293;</h1>
                </div>
            </div>
            <div className='flex items-center gap-2 bg-white/50 px-4 py-2 rounded-2xl'>
                <svg className='w-5 h-5 text-gray-500' fill='none' stroke='currentColor' viewBox='0 0 24 24'>
                    <path
                        strokeLinecap='round'
                        strokeLinejoin='round'
                        strokeWidth={2}
                        d='M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z'
                    />
                </svg>
                <input
                    type='text'
                    placeholder='Search for a job...'
                    className='bg-transparent outline-none text-gray-500 w-64'
                />
            </div>
        </>
    );
};

export default Header;
