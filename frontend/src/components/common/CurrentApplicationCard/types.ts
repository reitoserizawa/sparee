import type {
    CompanyJobApplicationWithoutUser,
    JobApplicationStatus,
} from '../../../store/features/jobApplication/types';

export interface CurrentApplicationCardProps {
    application: CompanyJobApplicationWithoutUser;
    onStatusChange: (applicationId: number, newStatus: JobApplicationStatus) => Promise<void>;
}
