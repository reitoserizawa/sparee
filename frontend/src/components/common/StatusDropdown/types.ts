import type { JobApplicationStatus } from '../../../store/features/jobApplication/types';

export interface StatusDropdownProps {
    current: JobApplicationStatus;
    onChange: (status: JobApplicationStatus) => void;
    isSaving: boolean;
}
