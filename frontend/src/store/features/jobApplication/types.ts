import type { SimpleJobPost } from '../jobPost/types';

type JobApplicationStatus = 'applied' | 'rejected' | 'reviewing' | 'withdrawn';

export interface JobApplication {
    id: number;
    application_status: JobApplicationStatus;
    job_post: SimpleJobPost;
    created_at: string;
}

export interface SimpleJobApplication {
    id: number;
    application_status: JobApplicationStatus;
    job_post_id: number;
    user_id: number;
    created_at: string;
}

export interface CreateJobApplicationRequest {
    jobPostId: number;
}

export interface DeleteJobApplicationRequest {
    jobApplicationId: number;
}

export interface UpdateJobApplicationStatusRequest {
    jobApplicationId: number;
    newStatus: JobApplicationStatus;
}
