import { createSlice, type PayloadAction } from '@reduxjs/toolkit';
import type { AuthState } from './types';

const initialState: AuthState = {
    username: null,
    accessToken: null,
};

const authSlice = createSlice({
    name: 'auth',
    initialState,
    reducers: {
        setCredentials: (state, action: PayloadAction<{ username: string; access_token: string }>) => {
            state.username = action.payload.username;
            state.accessToken = action.payload.access_token;
        },
        logout: state => {
            state.username = null;
            state.accessToken = null;
        },
    },
});

export const { setCredentials, logout } = authSlice.actions;
export default authSlice.reducer;
