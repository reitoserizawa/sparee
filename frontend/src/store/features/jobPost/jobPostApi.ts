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
            providesTags: result => (result ? result.map(({ id }) => ({ type: 'JobPost' as const, id })) : []),
        }),
        getAppliedJobPosts: builder.query<JobPost[], null>({
            query: () => ({
                url: `/job-posts/applied`,
                method: 'GET',
            }),
            providesTags: result => (result ? result.map(({ id }) => ({ type: 'JobPost' as const, id })) : []),
        }),
        getJobPostDetails: builder.query<JobPost, JobPostState>({
            query: ({ jobPostId }) => ({
                url: `/job-posts/${jobPostId}`,
                method: 'GET',
            }),
            providesTags: (result, error, { jobPostId }) => [{ type: 'JobPost', id: jobPostId }],
        }),
    }),
});

export const { useGetNearestJobPostsQuery, useGetJobPostDetailsQuery, useGetAppliedJobPostsQuery } = jobPostApi;
