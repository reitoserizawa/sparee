import type { JobPost } from '../jobPost/types';

export interface JobApplication {
    id: number;
    status: string;
    job_post: JobPost;
}

export interface SimpleJobApplication {
    id: number;
    status: string;
    job_post_id: JobPost;
    user_id: JobPost;
}

export interface JobApplicationCreate {
    jobPostId: number;
}
