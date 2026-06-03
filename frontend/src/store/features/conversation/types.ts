import type { SimpleUserResponse } from '../user/types';

export interface Message {
    id: number;
    sender_id: number;
    body: string;
    is_read: boolean;
    read_at: string | null;
    created_at: string;
}

export interface Conversation {
    id: number;
    applicant: SimpleUserResponse;
    participants: SimpleUserResponse[];
    messages: Message[];
    unread_count: number;
    created_at: string;
}
