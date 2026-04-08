import type { CompanyResponse } from '../company/type';

export interface AuthState {
    user: UserResponse | null;
    accessToken: string | null;
}

export interface AuthResponse {
    user: UserResponse;
    access_token: string;
}

export interface UserResponse {
    id: number;
    username: string;
    email: string;
    companies: CompanyResponse[] | null;
    created_at: string;
    updated_at: string;
}

export interface UserCreateState {
    username: string;
    email: string;
    password: string;
    confirm_password: string;
}

export interface UserLoginState {
    email: string;
    password: string;
}
