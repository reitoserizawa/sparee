import type { SimpleJobPost } from '../jobPost/types';
import type { SimpleUserResponse } from '../user/types';

type JobApplicationStatus = 'applied' | 'rejected' | 'reviewing' | 'withdrawn';

export interface JobApplication {
    id: number;
    application_status: JobApplicationStatus;
    job_post_id: number;
    job_post: SimpleJobPost;
    created_at: string;
    updated_at: string;
}

export interface SimpleJobApplication {
    id: number;
    application_status: JobApplicationStatus;
    job_post_id: number;
    user_id: number;
    created_at: string;
    updated_at: string;
}

export interface CompanyJobApplication {
    id: number;
    application_status: JobApplicationStatus;
    job_post_id: number;
    job_post: SimpleJobPost;
    user: SimpleUserResponse;
    created_at: string;
    updated_at: string;
}

export interface CreateJobApplicationRequest {
    jobPostId: number;
}

export interface GetJobApplicationsFromJobPostRequest {
    companyId: number;
    jobPostId: number;
}

export interface DeleteJobApplicationRequest {
    jobApplicationId: number;
}

export interface UpdateJobApplicationStatusRequest {
    jobApplicationId: number;
    newStatus: JobApplicationStatus;
}

export interface JobApplicationActivityDateRange {
    start: string;
    end: string;
}

export interface JobApplicationActivityDay {
    date: string;
    applied?: number;
    reviewing?: number;
    accepted?: number;
    withdrawn?: number;
    rejected?: number;
    total: number;
}
