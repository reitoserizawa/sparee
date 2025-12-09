import React from 'react';
import { Link } from 'react-router-dom';

const NavBar: React.FC = () => {
  return (
    <nav className='fixed w-full bg-white border-b px-6 py-4 shadow-sm sticky top-0 z-50'>
      <div className='max-w-7xl mx-auto flex items-center justify-between'>
        {/* Logo */}
        <div className='text-2xl font-bold tracking-tight text-gray-900'>MyApp</div>

        {/* Links */}
        <div className='flex items-center gap-8'>
          <Link to='/' className='text-gray-600 hover:text-gray-900 transition font-medium'>
            Home
          </Link>
          <Link to='/about' className='text-gray-600 hover:text-gray-900 transition font-medium'>
            About
          </Link>
          <Link to='/contact' className='text-gray-600 hover:text-gray-900 transition font-medium'>
            Contact
          </Link>
        </div>
      </div>
    </nav>
  );
};

export default NavBar;
