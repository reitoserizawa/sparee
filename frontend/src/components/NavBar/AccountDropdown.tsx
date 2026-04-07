import React, { useEffect, useRef } from 'react';
import { useNavigate } from 'react-router-dom';
import { useAppDispatch } from '../../store/hooks';
import { logout } from '../../store/features/auth/authSlice';

interface AccountDropdownProps {
    user: { name: string; email: string };
    onClose: () => void;
}

const AccountDropdown: React.FC<AccountDropdownProps> = ({ user, onClose }) => {
    const dropdownRef = useRef<HTMLDivElement>(null);
    const navigate = useNavigate();
    const dispatch = useAppDispatch();

    const handleLogout = () => {
        dispatch(logout());
        navigate('/login');
        onClose();
    };

    useEffect(() => {
        const handleClickOutside = (event: MouseEvent) => {
            if (dropdownRef.current && !dropdownRef.current.contains(event.target as Node)) {
                onClose();
            }
        };
        document.addEventListener('mousedown', handleClickOutside);
        return () => document.removeEventListener('mousedown', handleClickOutside);
    }, [onClose]);

    return (
        <div ref={dropdownRef} className='absolute right-0 mt-2 w-48 bg-white border rounded shadow-lg z-50'>
            <div className='px-4 py-2 border-b'>
                <p className='font-semibold'>{user.name}</p>
                <p className='text-sm text-gray-500'>{user.email}</p>
            </div>
            <div className='px-4 py-2 border-b' onClick={() => navigate('/company-register')}>
                <p>Create a company</p>
            </div>
            <button onClick={handleLogout} className='w-full text-left px-4 py-2 hover:bg-neutral-tertiary'>
                Logout
            </button>
        </div>
    );
};

export default AccountDropdown;
