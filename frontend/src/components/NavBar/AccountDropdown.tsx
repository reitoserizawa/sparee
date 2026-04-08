import React, { useEffect, useRef } from 'react';
import { useNavigate } from 'react-router-dom';
import { useAppDispatch } from '../../store/hooks';
import { logout } from '../../store/features/auth/authSlice';
import type { UserResponse } from '../../store/features/auth/types';

interface AccountDropdownProps {
    user: UserResponse;
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

    const handleNavigate = (path: string) => {
        navigate(path);
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
        <div ref={dropdownRef} className='absolute right-0 mt-2 w-50 bg-white border rounded shadow-lg z-50'>
            <div className='px-4 py-2 border-b'>
                <p className='font-semibold'>{user.username}</p>
                <p className='text-sm text-gray-500'>{user.email}</p>
            </div>
            <div className='py-1 border-b'>
                {user?.companies && user?.companies?.length > 0 && (
                    <>
                        {/* Show first 2 companies */}
                        {user?.companies.slice(0, 2).map(company => (
                            <button
                                key={company.id}
                                onClick={() => handleNavigate(`/companies/${company.id}`)}
                                className='w-full text-left px-4 py-2 hover:bg-neutral-tertiary'
                            >
                                🏢 {company.name}
                            </button>
                        ))}

                        {/* If more companies */}
                        {user.companies.length > 2 && (
                            <button
                                onClick={() => handleNavigate('/companies')}
                                className='w-full text-left px-4 py-2 text-sm text-gray-500 hover:bg-neutral-tertiary'
                            >
                                View all companies →
                            </button>
                        )}
                    </>
                )}
                <button
                    onClick={() => handleNavigate('/company-register')}
                    className='w-full text-left px-4 py-2 hover:bg-neutral-tertiary'
                >
                    ➕ Create Company
                </button>
            </div>
            <button onClick={handleLogout} className='w-full text-left px-4 py-2 hover:bg-neutral-tertiary'>
                Logout
            </button>
        </div>
    );
};

export default AccountDropdown;
