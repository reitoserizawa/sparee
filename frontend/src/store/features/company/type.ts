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
