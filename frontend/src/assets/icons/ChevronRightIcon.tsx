import type React from 'react';
import type { IconProps } from './types';

const ChevronRightIcon: React.FC<IconProps> = ({ size, className }) => (
    <svg viewBox='0 -960 960 960' width={size} height={size} fill='currentColor' className={className}>
        <path d='M504-480 320-664l56-56 240 240-240 240-56-56 184-184Z' />
    </svg>
);

export default ChevronRightIcon;
