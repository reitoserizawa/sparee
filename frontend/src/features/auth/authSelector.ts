import type { RootState } from '../../apps/store';

export const selectAuth = (state: RootState) => state.auth;
export const selectCurrentUser = (state: RootState) => state.auth.username;
export const selectAccessToken = (state: RootState) => state.auth.accessToken;
