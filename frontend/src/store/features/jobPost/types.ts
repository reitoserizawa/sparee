import type { AddressCreateState } from '../company/type';
import type { SimpleJobApplication } from '../jobApplication/types';

export interface JobPostGetDetailsState {
    jobPostId: number;
}

export interface JobPostCreateState {
    company_id: number;
    job_category_id?: number;
    title: string;
    description: string;
    salary: number;
    address?: AddressCreateState;
}

export interface JobPost {
    id: number;
    title: string;
    description: string;
    company: Company;
    skills?: string[];
    applications?: SimpleJobApplication[];
    salary: number;
    location?: string;
    address: Address;
    salary_type: string;
    job_category: JobPostCategory;
    application_status?: string;
    user_application?: SimpleJobApplication | null;
    created_at: string;
}

export interface CompanyJobPost extends JobPost {
    application_count: number;
}

export interface SimpleJobPost {
    id: number;
    title: string;
    description: string;
    skills?: string[];
    salary: number;
    location?: string;
    salary_type: string;
    application_status?: string;
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
