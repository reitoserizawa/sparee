import React from 'react';

const locations = ['New York', 'Los Angeles', 'San Francisco'];

const Sidebar: React.ElementType = () => {
    return (
        <>
            <div className='bg-white/50 backdrop-blur-xl rounded-3xl p-6'>
                <h3 className='font-semibold mb-4'>Salary Range</h3>
                <div className='space-y-3'>
                    <div className='flex items-center justify-between'>
                        <span>$50k</span>
                        <div className='w-20 h-2 bg-white/30 rounded-full'>
                            <div className='w-3/4 h-2 bg-gradient-to-r from-green-400 to-blue-500 rounded-full' />
                        </div>
                        <span>$150k</span>
                    </div>
                    <div className='flex items-center gap-2 text-sm opacity-90'>
                        <input
                            type='range'
                            min='50'
                            max='150'
                            className='flex-1 h-2 bg-white/30 rounded-lg appearance-none cursor-pointer accent-indigo-400 hover:accent-indigo-300'
                        />
                        <span>$90k</span>
                    </div>
                </div>
                <div className='flex flex-wrap gap-2 mt-6'>
                    {['Entry Level', 'Mid Level', 'Senior Level'].map(level => (
                        <button
                            key={level}
                            className='px-3 py-1 bg-white/20 rounded-xl text-xs hover:bg-white/30 transition-all'
                        >
                            {level}
                        </button>
                    ))}
                </div>
            </div>

            {/* Locations */}
            <div className='bg-white/50 backdrop-blur-xl rounded-3xl p-6'>
                <h3 className='font-semibold mb-4'>Location</h3>
                <div className='space-y-2'>
                    {locations.map(loc => (
                        <label
                            key={loc}
                            className='flex items-center gap-3 p-2 rounded-xl hover:bg-white/10 cursor-pointer'
                        >
                            <input type='checkbox' className='w-4 h-4 accent-white rounded' />
                            <span className='text-sm'>{loc}</span>
                        </label>
                    ))}
                </div>
            </div>

            {/* Hot Jobs Button */}
            <button className='w-full bg-gradient-to-r from-orange-500 to-red-500 hover:from-orange-400 hover:to-red-400 text-white font-semibold py-4 px-6 rounded-2xl  transform hover:-translate-y-1 transition-all duration-200'>
                🔥 Hot Jobs
            </button>
        </>
    );
};

export default Sidebar;
