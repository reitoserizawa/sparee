import type React from 'react';
import type { IconProps } from './types';

const CheckIcon: React.FC<IconProps> = ({ size, color }) => (
    <svg viewBox='0 -960 960 960' height={size} width={size} fill={color}>
        <path d='M382-240 154-468l57-57 171 171 367-367 57 57-424 424Z' />
    </svg>
);

export default CheckIcon;
