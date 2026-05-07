import React from 'react';
import type { StatCardProps } from './types';

const StatCard: React.FC<StatCardProps> = ({ label, value, sub }) => (
    <div className='bg-white border border-gray-200 rounded-xl px-5 py-4'>
        <p className='text-xs font-semibold tracking-widest text-gray-400 uppercase mb-1'>{label}</p>
        <p className='text-2xl font-bold text-gray-900 leading-none'>{value}</p>
        {sub && <p className='text-xs text-gray-400 mt-1'>{sub}</p>}
    </div>
);

export default StatCard;
