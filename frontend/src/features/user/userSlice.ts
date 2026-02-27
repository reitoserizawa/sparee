import { createSlice, type PayloadAction } from '@reduxjs/toolkit';
import type { UserState } from './types';

const initialState: UserState = {
    location: {
        lng: null,
        lat: null,
    },
};

const userSlice = createSlice({
    name: 'user',
    initialState,
    reducers: {
        setLocation: (state, action: PayloadAction<{ lng: number; lat: number }>) => {
            state.location = { lng: action.payload.lng, lat: action.payload.lat };
        },
        resetLocation: state => {
            state.location = { lng: null, lat: null };
        },
    },
});

export const { setLocation, resetLocation } = userSlice.actions;
export default userSlice.reducer;
