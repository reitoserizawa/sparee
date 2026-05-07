import type { CompanyJobApplicationWithoutUser } from '../../../store/features/jobApplication/types';

export interface ApplicationRowProps {
    app: CompanyJobApplicationWithoutUser;
    onEdit: (app: CompanyJobApplicationWithoutUser) => void;
    index: number;
}
