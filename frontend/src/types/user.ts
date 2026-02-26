export interface UserLoginFormState {
    email: string;
    password: string;
}

export interface UserCreateFormState {
    name: string;
    email: string;
    password: string;
    confirmPassword: string;
}

export interface UserTokenResponse {
    username: string;
    access_token: string;
}

export interface UserResponse {
    id: number;
    username: string;
    email: string;
}
