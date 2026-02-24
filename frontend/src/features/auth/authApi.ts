import baseApi from '../../services/baseApi';
import type { UserLoginRequest, UserTokenResponse } from '../../types/user';
import { setCredentials } from './authSlice';

const authApi = baseApi.injectEndpoints({
    endpoints: builder => ({
        login: builder.mutation<UserTokenResponse, UserLoginRequest>({
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
