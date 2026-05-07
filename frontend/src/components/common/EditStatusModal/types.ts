import type { CompanyJobApplication, JobApplicationStatus } from '../../../store/features/jobApplication/types';

export interface EditStatusModalProps {
    open: boolean;
    application: CompanyJobApplication;
    onClose: () => void;
    onSave: (applicationId: number, newStatus: JobApplicationStatus) => Promise<void>;
    isSaving: boolean;
}
