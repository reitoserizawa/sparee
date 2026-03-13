import type { JobPost } from '../jobPost/types';

export interface JobApplication {
    id: number;
    status: string;
    job_post: JobPost;
}

export interface SimpleJobApplication {
    id: number;
    status: string;
    job_post_id: number;
    user_id: number;
}

export interface JobApplicationCreate {
    jobPostId: number;
}

export interface JobApplicationDelete {
    jobApplicationId: number;
}
