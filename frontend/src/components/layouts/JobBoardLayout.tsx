import React from 'react';

interface JobBoardLayoutProps {
    header?: React.ReactNode;
    sidebar?: React.ReactNode;
    children: React.ReactNode;
}

const JobBoardLayout: React.FC<JobBoardLayoutProps> = ({ header, sidebar, children }) => {
    return (
        <div className='w-screen-xl min-h-[calc(100vh-61px)] bg-gradient-to-br bg-gray-200 flex flex-col'>
            <div className='max-w-7xl mx-auto pt-7'>
                {header && (
                    <header className='flex flex-col md:flex-row md:items-center md:justify-between mb-8 gap-6'>
                        {header}
                    </header>
                )}

                <div className='flex flex-1 overflow-hidden'>
                    {sidebar && <div className='lg:col-span-1 space-y-6'>{sidebar}</div>}

                    <main className='flex-1 overflow-y-auto p-6'>{children}</main>
                </div>
            </div>
        </div>
    );
};

export default JobBoardLayout;
