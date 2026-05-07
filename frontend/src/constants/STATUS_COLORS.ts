import type { JobApplicationStatus } from '../store/features/jobApplication/types';

export const STATUSES: JobApplicationStatus[] = ['applied', 'reviewing', 'rejected', 'withdrawn'];

export const STATUS_CONFIG: Record<
    JobApplicationStatus,
    { label: string; dot: string; badge: string; border: string; glow: string; ring: string }
> = {
    applied: {
        label: 'Applied',
        dot: 'bg-blue-500',
        badge: 'bg-blue-50 text-blue-700 border-blue-200',
        border: 'border-blue-200',
        glow: 'shadow-blue-100',
        ring: 'ring-blue-400',
    },
    reviewing: {
        label: 'Reviewing',
        dot: 'bg-amber-500',
        badge: 'bg-amber-50 text-amber-700 border-amber-200',
        border: 'border-amber-200',
        glow: 'shadow-amber-100',
        ring: 'ring-amber-400',
    },
    accepted: {
        label: 'Accepted',
        dot: 'bg-emerald-500',
        badge: 'bg-emerald-50 text-emerald-700 border-emerald-200',
        border: 'border-emerald-200',
        glow: 'shadow-emerald-100',
        ring: 'ring-emerald-400',
    },
    rejected: {
        label: 'Rejected',
        dot: 'bg-red-500',
        badge: 'bg-red-50 text-red-700 border-red-200',
        border: 'border-red-200',
        glow: 'shadow-red-100',
        ring: 'ring-red-400',
    },
    withdrawn: {
        label: 'Withdrawn',
        dot: 'bg-gray-500',
        badge: 'bg-gray-50 text-gray-700 border-gray-200',
        border: 'border-gray-200',
        glow: 'shadow-gray-100',
        ring: 'ring-gray-400',
    },
};
