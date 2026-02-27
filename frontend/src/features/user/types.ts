export interface UserState {
    location: UserLocationState;
}

export interface UserLocationState {
    lng: number | null;
    lat: number | null;
}
