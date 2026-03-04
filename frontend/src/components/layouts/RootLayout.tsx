import React from 'react';
import { Outlet } from 'react-router-dom';

import useUserLocation from '../../hooks/useUserLocation';

import NavBar from '../NavBar';

const RootLayout: React.FC = () => {
    useUserLocation();

    return (
        <>
            <NavBar />
            <main className='mt-[61px]'>
                <Outlet />
            </main>
        </>
    );
};

export default RootLayout;
