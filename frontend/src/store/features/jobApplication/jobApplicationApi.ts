import baseApi from '../base/baseApi';
import type { JobApplication } from './types';

const jobPostApi = baseApi.injectEndpoints({
    endpoints: builder => ({
        getUserJobApplications: builder.query<JobApplication[], null>({
            query: () => ({
                url: `/job-applications/me`,
                method: 'GET',
            }),
        }),
    }),
});

export const { useGetUserJobApplicationsQuery } = jobPostApi;
