import React from 'react';
import type { ButtonProps } from './types';

const Button: React.FC<ButtonProps> = ({
    children,
    type = 'button',
    variant = 'primary',
    disabled = false,
    className = '',
    onClick,
}): React.ReactElement => {
    const baseStyles =
        'flex items-center justify-center font-medium transition disabled:opacity-50 disabled:cursor-not-allowed';

    const variants = {
        primary: 'bg-black text-white hover:opacity-90',
        secondary: 'border border-gray-300 text-black hover:bg-gray-50',
        brand: 'bg-blue-600 text-white hover:bg-blue-700',
        ghost: 'text-gray-700 hover:bg-gray-100',
        danger: 'bg-red-600 text-white hover:bg-red-700',
        link: 'text-blue-600 hover:underline p-0',
    };

    return (
        <button
            type={type}
            disabled={disabled}
            onClick={onClick}
            className={`${baseStyles} ${variants[variant]} ${className}`}
        >
            {children}
        </button>
    );
};

export default Button;
