export interface UserState {
    location: UserLocationState;
}

export interface UserLocationState {
    lng: number | null;
    lat: number | null;
}

export interface SimpleUserResponse {
    id: number;
    username: string;
    email: string;
    created_at: string;
    updated_at: string;
}
