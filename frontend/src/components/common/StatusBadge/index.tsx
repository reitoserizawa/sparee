import { STATUS_CONFIG } from '../../../constants/STATUS_COLORS';
import type { ApplicationStatus } from './types';

const StatusBadge: React.FC<{ status: ApplicationStatus }> = ({ status }) => (
    <span
        className={`inline-flex items-center px-2 py-0.5 rounded-md text-xs font-medium capitalize ${STATUS_CONFIG[status].badge}`}
    >
        {status}
    </span>
);

export default StatusBadge;
