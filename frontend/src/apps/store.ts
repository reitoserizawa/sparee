import { configureStore } from '@reduxjs/toolkit';
import authReducer from '../features/auth/authSlice';
import userReducer from '../features/user/userSlice';
import baseApi from '../services/baseApi';

const store = configureStore({
    reducer: {
        auth: authReducer,
        user: userReducer,
        [baseApi.reducerPath]: baseApi.reducer,
    },
    middleware: getDefaultMiddleware => {
        return getDefaultMiddleware().concat(baseApi.middleware);
    },
});

export type RootState = ReturnType<typeof store.getState>;
export type AppDispatch = typeof store.dispatch;

export default store;
