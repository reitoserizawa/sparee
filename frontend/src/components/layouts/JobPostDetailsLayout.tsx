import React from 'react';

interface JobPostDetailsLayoutProps {
    sidebar: React.ReactNode;
    children: React.ReactNode;
}

const JobPostDetailsLayout: React.FC<JobPostDetailsLayoutProps> = ({ sidebar, children }) => {
    return (
        <div className='bg-gray-50 min-h-[calc(100vh-61px)]'>
            <div className='max-w-6xl mx-auto px-6 py-8 flex'>
                <div className='flex flex-1 gap-8'>
                    {/* MAIN CONTENT */}
                    <div className='flex-1'>{children}</div>

                    {/* RIGHT SIDEBAR */}
                    <div className='w-80 space-y-6 sticky top-24 self-start'>{sidebar}</div>
                </div>
            </div>
        </div>
    );
};

export default JobPostDetailsLayout;
