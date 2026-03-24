import type { JobApplicationActivityDay } from '../../../../store/features/jobApplication/types';

export type ActivityCalendarProps = {
    data: JobApplicationActivityDay[];
    onDayClick?: (date: string) => void;
};
