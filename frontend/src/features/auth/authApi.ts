import baseApi from '../../services/baseApi';
import type { UserLoginFormState, UserTokenResponse } from '../../types/user';
import { setCredentials } from './authSlice';

const authApi = baseApi.injectEndpoints({
    endpoints: builder => ({
        login: builder.mutation<UserTokenResponse, UserLoginFormState>({
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
    }),
});

export const { useLoginMutation } = authApi;
