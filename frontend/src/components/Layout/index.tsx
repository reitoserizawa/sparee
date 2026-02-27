import React from 'react';
import { Outlet } from 'react-router-dom';

import useUserLocation from '../../hooks/useUserLocation';

import NavBar from './NavBar';

const Layout: React.FC = () => {
    useUserLocation();

    return (
        <>
            <NavBar />
            <main className='max-w-7xl mt-[61px] px-4 py-6'>
                <Outlet />
            </main>
        </>
    );
};

export default Layout;
