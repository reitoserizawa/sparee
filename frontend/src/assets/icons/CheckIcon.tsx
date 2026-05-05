import type React from 'react';
import type { IconProps } from './types';

const CheckIcon: React.FC<IconProps> = ({ size, className }) => (
    <svg viewBox='0 -960 960 960' width={size} height={size} fill='currentColor' className={className}>
        <path d='M382-240 154-468l57-57 171 171 367-367 57 57-424 424Z' />
    </svg>
);

export default CheckIcon;
