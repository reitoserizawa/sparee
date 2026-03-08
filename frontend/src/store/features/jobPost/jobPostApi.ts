import baseApi from '../base/baseApi';
import type { UserLocationState } from '../user/types';
import type { JobPost, JobPostState } from './types';

const jobPostApi = baseApi.injectEndpoints({
    endpoints: builder => ({
        getNearestJobPosts: builder.query<JobPost[], UserLocationState>({
            query: ({ lng, lat }) => ({
                url: `/job-posts/nearest?lng=${lng}&lat=${lat}`,
                method: 'GET',
            }),
        }),
        getJobPostDetails: builder.query<JobPost, JobPostState>({
            query: ({ jobPostId }) => ({
                url: `/job-posts/${jobPostId}`,
                method: 'GET',
            }),
        }),
    }),
});

export const { useGetNearestJobPostsQuery, useGetJobPostDetailsQuery } = jobPostApi;
