import { useMemo, useState } from 'react';
import type { ActivityCalendarProps } from './types';
import type { JobApplicationActivityDay } from '../../../../store/features/jobApplication/types';
import DateUtils from '../../../../utils/DateUtils';
import { useGetJobApplicationActivityQuery } from '../../../../store/features/jobApplication/jobApplicationApi';

const ActivityCalendar: React.FC<ActivityCalendarProps> = ({ onDayClick }) => {
    const [currentDate, setCurrentDate] = useState(new Date());
    const [hovered, setHovered] = useState<JobApplicationActivityDay | null>(null);

    const startOfMonth = useMemo(() => {
        const d = new Date(currentDate.getFullYear(), currentDate.getMonth(), 1);
        d.setHours(0, 0, 0, 0);
        return d;
    }, [currentDate]);

    const endOfMonth = useMemo(() => {
        const d = new Date(currentDate.getFullYear(), currentDate.getMonth() + 1, 0);
        d.setHours(23, 59, 59, 999);
        return d;
    }, [currentDate]);

    const { data } = useGetJobApplicationActivityQuery({
        start: startOfMonth.toISOString(),
        end: endOfMonth.toISOString(),
    });

    const today = new Date();
    const todayStr = DateUtils.formatDate(today);

    const activityMap = useMemo(() => {
        const map = new Map<string, JobApplicationActivityDay>();
        data?.forEach(d => map.set(d.date, d));
        return map;
    }, [data]);

    const days = useMemo(() => {
        const year = currentDate.getFullYear();
        const month = currentDate.getMonth();

        const firstDay = new Date(year, month, 1);
        const startDay = firstDay.getDay();

        const lastDay = new Date(year, month + 1, 0);
        const totalDays = lastDay.getDate();

        const totalCells = startDay + totalDays;
        const totalWeeks = Math.ceil(totalCells / 7);
        const totalGridCells = totalWeeks * 7;

        const startDate = new Date(year, month, 1);
        startDate.setDate(startDate.getDate() - startDay);

        const result: { date: string; isCurrentMonth: boolean }[] = [];

        for (let i = 0; i < totalGridCells; i++) {
            const d = new Date(startDate);
            d.setDate(startDate.getDate() + i);

            result.push({
                date: DateUtils.formatDate(d),
                isCurrentMonth: d.getMonth() === month,
            });
        }

        return result;
    }, [currentDate]);

    const getColor = (day?: JobApplicationActivityDay) => {
        if (!day || day.total === 0) return 'bg-gray-100';
        if (day.total < 2) return 'bg-green-200';
        if (day.total < 4) return 'bg-green-400';
        return 'bg-green-600';
    };

    const goMonth = (offset: number) => {
        setCurrentDate(prev => {
            const newDate = new Date(prev);
            newDate.setMonth(newDate.getMonth() + offset);
            return newDate;
        });
    };

    return (
        <div className='w-full transition-all duration-300 relative'>
            {/* header */}
            <div className='flex items-center justify-between mb-4'>
                <button onClick={() => goMonth(-1)} className='px-2 py-1 rounded-md hover:bg-gray-100 transition'>
                    ←
                </button>

                <h3 className='text-sm font-semibold'>
                    {currentDate.toLocaleString('default', {
                        month: 'long',
                        year: 'numeric',
                    })}
                </h3>

                <button onClick={() => goMonth(1)} className='px-2 py-1 rounded-md hover:bg-gray-100 transition'>
                    →
                </button>
            </div>

            {/* week label */}
            <div className='grid grid-cols-7 text-xs text-gray-400 mb-1'>
                {['S', 'M', 'T', 'W', 'T', 'F', 'S'].map((d, idx) => (
                    <div key={idx} className='text-center'>
                        {d}
                    </div>
                ))}
            </div>

            {/* calendar */}
            <div className='grid grid-cols-7 gap-2'>
                {days.map(({ date, isCurrentMonth }) => {
                    const day = activityMap.get(date);
                    const current = DateUtils.parseDate(date);

                    const isToday = date === todayStr;
                    const isFuture = current > today;

                    return (
                        <div
                            key={date}
                            onClick={() => !isFuture && onDayClick?.(date)}
                            onMouseEnter={() => setHovered(day || null)}
                            onMouseLeave={() => setHovered(null)}
                            className={`
                                h-8 w-8 rounded-lg flex items-center justify-center text-[11px] font-medium
                                ${getColor(day)}
                                ${!isCurrentMonth ? 'opacity-40' : ''}
                                ${isFuture ? 'opacity-30 cursor-not-allowed' : 'cursor-pointer'}
                                transition-all duration-200
                                ${!isFuture ? 'hover:scale-110 hover:ring-2 hover:ring-black/10' : ''}
                                ${isToday ? 'ring-2 ring-black' : ''}
                            `}
                        >
                            {current.getDate()}
                        </div>
                    );
                })}
            </div>

            {/* tooltip */}
            {hovered && (
                <div className='absolute top-full left-1/2 -translate-x-1/2 mt-3 w-56 rounded-xl bg-white shadow-xl p-3 text-xs border z-50'>
                    <p className='text-gray-500 mb-1'>{DateUtils.parseDate(hovered.date).toDateString()}</p>
                    <p className='font-semibold mb-1'>{hovered.total} activities</p>
                    {hovered.applied && <p>📨 Applied: {hovered.applied}</p>}
                    {hovered.withdrawn && <p>🗑️ Withdrawn: {hovered.withdrawn}</p>}
                    {hovered.reviewing && <p>👀 Reviewing: {hovered.reviewing}</p>}
                    {hovered.accepted && <p>✅ Accepted: {hovered.accepted}</p>}
                    {hovered.rejected && <p>❌ Rejected: {hovered.rejected}</p>}
                </div>
            )}
        </div>
    );
};

export default ActivityCalendar;
