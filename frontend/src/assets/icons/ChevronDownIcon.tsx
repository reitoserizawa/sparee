import type React from 'react';
import type { IconProps } from './types';

const ChevronDownIcon: React.FC<IconProps> = ({ size, className }) => (
    <svg viewBox='0 -960 960 960' width={size} height={size} fill='currentColor' className={className}>
        <path d='M480-344 240-584l56-56 184 184 184-184 56 56-240 240Z' />
    </svg>
);

export default ChevronDownIcon;
