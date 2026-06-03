import baseApi from '../base/baseApi';
import type { Conversation } from './types';

const conversationApi = baseApi.injectEndpoints({
    endpoints: builder => ({
        getConversations: builder.query<Conversation[], null>({
            query: () => ({
                url: '/conversations',
                method: 'GET',
            }),
            providesTags: ['Conversation'],
        }),
    }),
});

export const { useGetConversationsQuery } = conversationApi;
