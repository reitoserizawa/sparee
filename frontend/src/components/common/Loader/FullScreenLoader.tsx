import React from 'react';

const FullscreenLoader = (): React.ReactElement => {
    return (
        <div className='fixed inset-0 z-50 flex items-center justify-center bg-gray-50'>
            <div className='flex flex-col items-center'>
                <div className='h-10 w-10 animate-spin rounded-full border-4 border-gray-200 border-t-black' />
                <p className='mt-4 text-sm text-gray-500'>Loading...</p>
            </div>
        </div>
    );
};

export default FullscreenLoader;
