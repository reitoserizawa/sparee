import type { SimpleUserResponse } from '../user/types';

export interface Message {
    id: number;
    sender_id: number;
    body: string;
    timestamp: string;
}

export interface Conversation {
    id: number;
    applicant: SimpleUserResponse;
    participants: SimpleUserResponse[];
    messages: Message[];
    created_at: string;
}
