import baseApi from '../base/baseApi';
import {
    type JobApplication,
    type CreateJobApplicationRequest,
    type DeleteJobApplicationRequest,
    type SimpleJobApplication,
    type ChangeJobApplicationStatusRequest,
    type JobApplicationActivityDay,
    type JobApplicationActivityDateRange,
    type GetJobApplicationsFromJobPostRequest,
    type CompanyJobApplication,
    type GetJobApplicationDetailsRequest,
    type SimpleCompanyJobApplication,
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
        createJobApplication: builder.mutation<JobApplication, CreateJobApplicationRequest>({
            query: ({ jobPostId }) => ({
                url: `/job-applications`,
                method: 'POST',
                body: {
                    job_post_id: jobPostId,
                },
            }),
            invalidatesTags: result => {
                if (!result) return [{ type: 'JobApplication', id: 'LIST' }];
                return [
                    { type: 'JobApplication', id: result.id },
                    { type: 'JobApplication', id: 'LIST' },
                    { type: 'JobPost', id: result.job_post_id },
                ];
            },
        }),
        deleteJobApplication: builder.mutation<SimpleJobApplication, DeleteJobApplicationRequest>({
            query: ({ jobApplicationId }) => ({
                url: `/job-applications/${jobApplicationId}`,
                method: 'DELETE',
            }),
            invalidatesTags: result => {
                if (!result) return [{ type: 'JobApplication', id: 'LIST' }];
                return [
                    { type: 'JobApplication', id: result.id },
                    { type: 'JobApplication', id: 'LIST' },
                    { type: 'JobPost', id: result.job_post_id },
                ];
            },
        }),
        getJobApplicationActivity: builder.query<JobApplicationActivityDay[], JobApplicationActivityDateRange>({
            query: ({ start, end }) => ({
                url: `/job-applications/activity`,
                method: 'GET',
                params: { start, end },
            }),
            providesTags: [{ type: 'JobApplication', id: 'LIST' }],
        }),
        getJobApplicationFromJobPost: builder.query<
            SimpleCompanyJobApplication[],
            GetJobApplicationsFromJobPostRequest
        >({
            query: ({ companyId, jobPostId }) => ({
                url: `/companies/${companyId}/job-posts/${jobPostId}/applications`,
            }),
        }),
        getJobApplicationDetails: builder.query<CompanyJobApplication, GetJobApplicationDetailsRequest>({
            query: ({ companyId, jobPostId, jobApplicationId }) => ({
                url: `/companies/${companyId}/job-posts/${jobPostId}/applications/${jobApplicationId}`,
            }),
        }),
        changeJobApplicationStatus: builder.mutation<SimpleJobApplication, ChangeJobApplicationStatusRequest>({
            query: ({ companyId, jobPostId, jobApplicationId, newStatus }) => ({
                url: `/companies/${companyId}/job-posts/${jobPostId}/applications/${jobApplicationId}`,
                method: 'PATCH',
                body: {
                    new_status: newStatus,
                },
            }),
            invalidatesTags: result => {
                if (!result) return [{ type: 'JobApplication', id: 'LIST' }];
                return [
                    { type: 'JobApplication', id: result.id },
                    { type: 'JobApplication', id: 'LIST' },
                    { type: 'JobPost', id: result.job_post_id },
                ];
            },
        }),
    }),
});

export const {
    useGetUserJobApplicationsQuery,
    useCreateJobApplicationMutation,
    useDeleteJobApplicationMutation,
    useChangeJobApplicationStatusMutation,
    useGetJobApplicationActivityQuery,
    useGetJobApplicationFromJobPostQuery,
    useGetJobApplicationDetailsQuery,
} = jobApplicationApi;
