export interface JobPostState {
    jobPostId: number;
}

export interface JobPost {
    id: number;
    title: string;
    description: string;
    company: Company;
    skills?: string[];
    salary: number;
    location?: string;
    address: Address;
    salary_type: string;
    job_category: JobPostCategory;
    created_at: string;
}

interface JobPostCategory {
    id: number;
    name: string;
}

interface Company {
    name: string;
    id: number;
    address: Address;
    created_at: string;
    updated_at: string;
}

interface Address {
    street: string;
    city: string;
    state: string;
    postal_code: string;
    country: string;
    id: number;
    coordinates?: {
        lat: number;
        lng: number;
    };
    full_address: string;
}
