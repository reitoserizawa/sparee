import React from 'react';
import type { ModalProps } from './types';

const Modal: React.FC<ModalProps> = ({ open, title, onClose, children }: ModalProps) => {
    if (!open) return null;

    return (
        <div className='fixed inset-0 z-50 flex items-center justify-center'>
            <div className='absolute inset-0 bg-black/40' onClick={onClose} />
            <div className='relative z-10 w-full max-w-md bg-white rounded-xl shadow-lg p-6'>
                {title && <h2 className='text-lg font-semibold mb-4'>{title}</h2>}

                {children}
            </div>
        </div>
    );
};

export default Modal;
