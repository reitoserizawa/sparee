export interface AuthState {
    username: string | null;
    email?: string;
    accessToken: string | null;
}

export interface AuthResponse {
    username: string;
    email?: string;
    access_token: string;
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
