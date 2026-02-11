import React from 'react';
import type { ErrorState } from './types';

const Error: React.FC<ErrorState> = ({ message = 'Unknown error occured' }) => {
    return (
        <div className='mt-2 rounded-md border border-red-500 bg-pink-200 p-2'>
            <div className='flex items-center gap-1'>
                <p className='m-0 text-red-600'>{message}</p>
            </div>
        </div>
    );
};

export default Error;
