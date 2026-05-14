import React from 'react';

const InlineLoader: React.FC = () => {
    return (
        <div className='flex items-center justify-center px-4 py-3'>
            <div className='h-4 w-4 animate-spin rounded-full border-2 border-gray-200 border-t-black' />
        </div>
    );
};

export default InlineLoader;
