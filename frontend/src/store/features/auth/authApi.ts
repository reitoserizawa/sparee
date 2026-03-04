import baseApi from '../base/baseApi';
import { setCredentials } from './authSlice';

import type { AuthResponse, UserLoginState, UserCreateState } from './types';

const authApi = baseApi.injectEndpoints({
    endpoints: builder => ({
        login: builder.mutation<AuthResponse, UserLoginState>({
            query: credentials => ({
                url: '/auth/login',
                method: 'POST',
                body: credentials,
            }),
            async onQueryStarted(arg, { dispatch, queryFulfilled }) {
                const { data } = await queryFulfilled;
                dispatch(setCredentials(data));
            },
        }),
        register: builder.mutation<AuthResponse, UserCreateState>({
            query: credentials => ({
                url: '/auth/register',
                method: 'POST',
                body: credentials,
            }),
            async onQueryStarted(arg, { dispatch, queryFulfilled }) {
                const { data } = await queryFulfilled;
                dispatch(setCredentials(data));
            },
        }),
        refresh: builder.mutation<AuthResponse, null>({
            query: () => ({
                url: '/auth/refresh',
                method: 'POST',
            }),
            async onQueryStarted(arg, { dispatch, queryFulfilled }) {
                const { data } = await queryFulfilled;
                dispatch(setCredentials(data));
            },
        }),
    }),
});

export const { useLoginMutation, useRegisterMutation, useRefreshMutation } = authApi;
