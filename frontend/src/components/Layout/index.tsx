import React from 'react';
import { Outlet } from 'react-router-dom';
import NavBar from './NavBar';

const Layout: React.FC = () => {
  return (
    <>
      <NavBar />
      <main className='max-w-7xl mx-auto px-4 py-6'>
        <Outlet />
      </main>
    </>
  );
};

export default Layout;
