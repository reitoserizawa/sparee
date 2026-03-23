import React from 'react';
import type { LoaderProps } from './types';

const FullscreenLoader: React.FC<LoaderProps> = ({ withNavBar = false }) => {
    return (
        <div
            className={
                'fixed inset-x-0 bottom-0 z-50 flex items-center justify-center bg-gray-50 ' +
                (withNavBar ? 'top-[61px]' : 'top-0')
            }
        >
            <div className='flex flex-col items-center'>
                <div className='h-10 w-10 animate-spin rounded-full border-4 border-gray-200 border-t-black' />
                <p className='mt-4 text-sm text-gray-500'>Loading...</p>
            </div>
        </div>
    );
};

export default FullscreenLoader;
