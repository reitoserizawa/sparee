import type React from 'react';
import type { IconProps } from './types';

const ArrowLeftIcon: React.FC<IconProps> = ({ size, className }) => (
    <svg viewBox='0 -960 960 960' width={size} height={size} fill='currentColor' className={className}>
        <path d='M400-240 160-480l240-240 56 58-142 142h486v80H314l142 142-56 58Z' />
    </svg>
);

export default ArrowLeftIcon;
