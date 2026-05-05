import React from 'react';
import type { ErrorState } from './types';
import WarningIcon from '../../../assets/icons/WarningIcon';

const Error: React.FC<ErrorState> = ({ message = 'Unknown error occured' }) => {
    return (
        <div className='flex items-center gap-1 rounded-lg border border-red-500 bg-pink-200 px-3 py-2 text-sm'>
            <WarningIcon size={14} className='text-red-600' />
            <p className='m-0 text-red-600'>{message}</p>
        </div>
    );
};

export default Error;
