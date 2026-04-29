import type { JobPostCreateState } from '../../../store/features/jobPost/types';

export interface CreateJobPostModalProps {
    onClose: () => void;
    onSubmit?: (data: JobPostCreateState) => void;
}
