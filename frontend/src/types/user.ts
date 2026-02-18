export interface UserLoginRequest {
    email: string;
    password: string;
}

export interface UserTokenResponse {
    username: string;
    token: string;
}

export interface UserResponse {
    id: number;
    username: string;
    email: string;
}
