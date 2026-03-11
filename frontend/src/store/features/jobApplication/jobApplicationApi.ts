import baseApi from '../base/baseApi';
import type { JobApplication, JobApplicationCreate } from './types';

const jobApplicationApi = baseApi.injectEndpoints({
    endpoints: builder => ({
        getUserJobApplications: builder.query<JobApplication[], null>({
            query: () => ({
                url: `/job-applications/me`,
                method: 'GET',
            }),
            providesTags: result =>
                result
                    ? [
                          ...result.map(({ id }) => ({ type: 'JobApplication' as const, id })),
                          { type: 'JobApplication', id: 'LIST' },
                      ]
                    : [{ type: 'JobApplication', id: 'LIST' }],
        }),
        createJobApplications: builder.mutation<JobApplication, JobApplicationCreate>({
            query: ({ jobPostId }) => ({
                url: `/job-applications`,
                method: 'POST',
                body: {
                    job_post_id: jobPostId,
                },
            }),
            invalidatesTags: (result, error, { jobPostId }) => [
                { type: 'JobApplication', id: 'LIST' },
                { type: 'JobPost', id: jobPostId },
            ],
        }),
    }),
});

export const { useGetUserJobApplicationsQuery, useCreateJobApplicationsMutation } = jobApplicationApi;
