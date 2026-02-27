import baseApi from '../../services/baseApi';
import type { UserLocationState } from '../user/types';
import type { JobPost } from './types';

const jobPostApi = baseApi.injectEndpoints({
    endpoints: builder => ({
        getNearestJobPosts: builder.query<JobPost[], UserLocationState>({
            query: ({ lng, lat }) => ({
                url: `/job-posts?lng=${lng}&lat=${lat}`,
                method: 'GET',
            }),
        }),
    }),
});

export const { useGetNearestJobPostsQuery } = jobPostApi;
