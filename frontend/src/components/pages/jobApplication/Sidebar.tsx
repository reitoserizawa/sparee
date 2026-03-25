import type React from 'react';
import Card from '../../ui/Card';
import ActivityCalendar from './ActivityCalendar/ActivityCalendar';

const Sidebar: React.FC<{ stats: Record<string, number> }> = ({ stats }) => {
    return (
        <>
            <Card>
                <h3 className='font-semibold mb-4'>Overview</h3>

                <div className='space-y-2 text-sm'>
                    <p>📨 Applied: {stats.applied || 0}</p>
                    <p>👀 Reviewing: {stats.reviewing || 0}</p>
                    <p>✅ Accepted: {stats.accepted || 0}</p>
                    <p>❌ Rejected: {stats.rejected || 0}</p>
                </div>
            </Card>
            <Card>
                <h3 className='font-semibold mb-4'>Activity</h3>
                <ActivityCalendar />
            </Card>
        </>
    );
};

export default Sidebar;
