// create types
export interface CompanyCreateState {
    name: string;
    address: AddressCreateState;
}

export interface AddressCreateState {
    street: string;
    city: string;
    state: string;
    postal_code: string;
    country: string;
}

// response types
export interface CompanyResponse {
    id: number;
    name: string;
    address: AddressResponse;
    created_at: string;
    updated_at: string;
}

export interface AddressResponse {
    id: number;
    full_address: string;
    street: string;
    city: string;
    state: string;
    postal_code: string;
    country: string;
    coordinates?: {
        lat: number;
        lng: number;
    };
}
