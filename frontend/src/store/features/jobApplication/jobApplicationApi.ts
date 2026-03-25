import baseApi from '../base/baseApi';
import {
    type JobApplication,
    type CreateJobApplicationRequest,
    type DeleteJobApplicationRequest,
    type SimpleJobApplication,
    type UpdateJobApplicationStatusRequest,
    type JobApplicationActivityDay,
    type JobApplicationActivityDateRange,
} from './types';

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
        createJobApplications: builder.mutation<JobApplication, CreateJobApplicationRequest>({
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
        deleteJobApplication: builder.mutation<SimpleJobApplication, DeleteJobApplicationRequest>({
            query: ({ jobApplicationId }) => ({
                url: `/job-applications/${jobApplicationId}`,
                method: 'DELETE',
            }),
            invalidatesTags: result => {
                if (!result) return [{ type: 'JobApplication', id: 'LIST' }];
                return [
                    { type: 'JobApplication', id: 'LIST' },
                    { type: 'JobPost', id: result.job_post_id },
                ];
            },
        }),
        changeJobApplicationStatus: builder.mutation<SimpleJobApplication, UpdateJobApplicationStatusRequest>({
            query: ({ jobApplicationId, newStatus }) => ({
                url: `/job-applications/${jobApplicationId}`,
                method: 'PATCH',
                body: {
                    new_status: newStatus,
                },
            }),
            invalidatesTags: result => {
                if (!result) return [{ type: 'JobApplication', id: 'LIST' }];
                return [
                    { type: 'JobApplication', id: 'LIST' },
                    { type: 'JobPost', id: result.job_post_id },
                ];
            },
        }),
        getJobApplicationActivity: builder.query<JobApplicationActivityDay[], JobApplicationActivityDateRange>({
            query: ({ start, end }) => ({
                url: `/job-applications/activity?start=${start}&end=${end}`,
                method: 'GET',
            }),
        }),
    }),
});

export const {
    useGetUserJobApplicationsQuery,
    useCreateJobApplicationsMutation,
    useDeleteJobApplicationMutation,
    useChangeJobApplicationStatusMutation,
    useGetJobApplicationActivityQuery,
} = jobApplicationApi;
