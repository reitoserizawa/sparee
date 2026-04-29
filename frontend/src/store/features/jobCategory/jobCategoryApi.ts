import baseApi from '../base/baseApi';
import { type JobCategory } from './types';

const jobCategoryApi = baseApi.injectEndpoints({
    endpoints: builder => ({
        getJobCategories: builder.query<JobCategory[], null>({
            query: () => ({
                url: `/job-categories`,
                method: 'GET',
            }),
            providesTags: [{ type: 'JobCategory', id: 'LIST' }],
        }),
    }),
});

export const { useGetJobCategoriesQuery } = jobCategoryApi;
