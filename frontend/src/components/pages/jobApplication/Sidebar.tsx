import type React from 'react';
import Card from '../../ui/Card';

const Sidebar: React.FC<{ stats: Record<string, number> }> = ({ stats }) => {
    return (
        <>
            {/* SUMMARY CARD */}
            <Card>
                <h3 className='font-semibold mb-4'>Overview</h3>

                <div className='space-y-2 text-sm'>
                    <p>📨 Applied: {stats.applied || 0}</p>
                    <p>👀 Reviewing: {stats.reviewing || 0}</p>
                    <p>✅ Accepted: {stats.accepted || 0}</p>
                    <p>❌ Rejected: {stats.rejected || 0}</p>
                </div>
            </Card>

            {/* SIMPLE CALENDAR / ACTIVITY */}
            <Card>
                <h3 className='font-semibold mb-4'>Activity</h3>

                <div className='grid grid-cols-7 gap-2 text-xs text-center'>
                    {Array.from({ length: 28 }).map((_, i) => (
                        <div key={i} className='h-6 w-6 rounded bg-gray-100 flex items-center justify-center'>
                            {i + 1}
                        </div>
                    ))}
                </div>
            </Card>
        </>
    );
};

export default Sidebar;
