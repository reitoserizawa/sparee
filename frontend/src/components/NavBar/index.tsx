import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import AccountCircle from '../../assets/icons/AccountCircle';
import AccountDropdown from './AccountDropdown';
import { selectAuth } from '../../store/features/auth/authSelector';
import { useAppSelector } from '../../store/hooks';

const NavBar: React.FC = () => {
    const [isDropdownOpen, setIsDropdownOpen] = useState(false);
    const auth = useAppSelector(selectAuth);

    const user = {
        name: auth?.username || 'John Doe',
        email: auth?.email || 'john@example.com',
    };

    return (
        <nav className='bg-white fixed w-full z-20 top-0 start-0 border-b border-default'>
            <div className='max-w-screen-xl flex flex-wrap items-center justify-between mx-auto p-4'>
                <span className='self-center text-xl text-heading font-semibold whitespace-nowrap'>Sparee</span>
                <div className='hidden w-full md:block md:w-auto'>
                    <ul className='font-medium flex flex-col p-4 md:p-0 mt-4 border border-default rounded-base bg-neutral-secondary-soft md:flex-row md:space-x-8 rtl:space-x-reverse md:mt-0 md:border-0 md:bg-neutral-primary'>
                        <li>
                            <Link
                                to='/jobs'
                                className='block py-2 px-3 text-heading rounded hover:bg-neutral-tertiary md:hover:bg-transparent md:border-0 md:hover:text-fg-brand md:p-0'
                            >
                                Jobs
                            </Link>
                        </li>
                        <li>
                            <Link
                                to='/applications'
                                className='block py-2 px-3 text-heading rounded hover:bg-neutral-tertiary md:hover:bg-transparent md:border-0 md:hover:text-fg-brand md:p-0'
                            >
                                Applications
                            </Link>
                        </li>
                        <li>
                            <Link
                                to='/'
                                className='block py-2 px-3 text-heading rounded hover:bg-neutral-tertiary md:hover:bg-transparent md:border-0 md:hover:text-fg-brand md:p-0'
                            >
                                Messages
                            </Link>
                        </li>
                        <li className='relative'>
                            <div
                                className='cursor-pointer block py-2 px-3 text-heading rounded hover:bg-neutral-tertiary md:hover:bg-transparent md:border-0 md:hover:text-fg-brand md:p-0 flex items-center'
                                onClick={() => setIsDropdownOpen(!isDropdownOpen)}
                            >
                                <AccountCircle size={24} color='black' />
                            </div>
                            {isDropdownOpen && <AccountDropdown user={user} onClose={() => setIsDropdownOpen(false)} />}
                        </li>
                    </ul>
                </div>
            </div>
        </nav>
    );
};

export default NavBar;
