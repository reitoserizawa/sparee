import baseApi from '../base/baseApi';

import type { CompanyCreateState, CompanyResponse } from './type';

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
    }),
});

export const { useCreateCompanyMutation } = companyApi;
