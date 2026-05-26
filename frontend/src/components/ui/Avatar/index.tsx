import React from 'react';
import type { AvatarProps } from './types';

const Avatar: React.FC<AvatarProps> = ({ initial, size = 'md', isOnline }) => {
    const sizeClasses = { sm: 'h-9 w-9 text-sm', md: 'h-10 w-10 text-base', lg: 'h-12 w-12 text-lg' };
    return (
        <div className='relative flex-shrink-0'>
            <div
                className={`${sizeClasses[size]} bg-blue-600 rounded-xl flex items-center justify-center text-white font-semibold`}
            >
                {initial}
            </div>
            {isOnline !== undefined && (
                <span
                    className={`absolute -bottom-0.5 -right-0.5 h-3 w-3 rounded-full border-2 border-white ${isOnline ? 'bg-green-400' : 'bg-gray-300'}`}
                />
            )}
        </div>
    );
};

export default Avatar;
