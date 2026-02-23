import baseApi from '../../services/baseApi';
import { setCredentials } from './authSlice';

const authApi = baseApi.injectEndpoints({
    endpoints: builder => ({
        login: builder.mutation<{ username: string; access_token: string }, { email: string; password: string }>({
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
