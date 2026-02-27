export interface AuthState {
    username: string | null;
    accessToken: string | null;
}

export interface AuthResponse {
    username: string;
    access_token: string;
}

export interface UserCreateState {
    name: string;
    email: string;
    password: string;
    confirmPassword: string;
}

export interface UserLoginState {
    email: string;
    password: string;
}
