import baseApi from '../base/baseApi';

import type { CompanyCreateState, CompanyResponse, SimpleCompanyResponse } from './type';

const companyApi = baseApi.injectEndpoints({
    endpoints: builder => ({
        createCompany: builder.mutation<CompanyResponse, CompanyCreateState>({
            query: data => ({
                url: '/companies',
                method: 'POST',
                body: data,
            }),
            invalidatesTags: ['Company'],
        }),
        getCompanies: builder.query<SimpleCompanyResponse[], null>({
            query: () => ({
                url: '/companies',
                method: 'GET',
            }),
            providesTags: ['Company'],
        }),
    }),
});

export const { useCreateCompanyMutation, useGetCompaniesQuery } = companyApi;
