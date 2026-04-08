import { createSlice, type PayloadAction } from '@reduxjs/toolkit';
import type { AuthResponse, AuthState } from './types';

const initialState: AuthState = {
    user: null,
    accessToken: null,
};

const authSlice = createSlice({
    name: 'auth',
    initialState,
    reducers: {
        setCredentials: (state, action: PayloadAction<AuthResponse>) => {
            state.user = action.payload.user;
            state.accessToken = action.payload.access_token;
        },
        logout: state => {
            state.user = null;
            state.accessToken = null;
        },
    },
});

export const { setCredentials, logout } = authSlice.actions;
export default authSlice.reducer;
