import type { ApplicationStatus } from './types';

const statusStyles: Record<ApplicationStatus, string> = {
    applied: 'bg-yellow-50 text-yellow-700 ring-1 ring-yellow-200',
    reviewing: 'bg-blue-50 text-blue-700 ring-1 ring-blue-200',
    accepted: 'bg-green-50 text-green-700 ring-1 ring-green-200',
    rejected: 'bg-red-50 text-red-700 ring-1 ring-red-200',
    withdrawn: 'bg-red-50 text-red-700 ring-1 ring-black-200',
};

const StatusBadge: React.FC<{ status: ApplicationStatus }> = ({ status }) => (
    <span
        className={`inline-flex items-center px-2 py-0.5 rounded-md text-xs font-medium capitalize ${statusStyles[status]}`}
    >
        {status}
    </span>
);

export default StatusBadge;
