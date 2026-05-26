import type { Conversation } from '../../../store/features/chat/types';

export interface ConversationItemProps {
    conversation: Conversation;
    isActive: boolean;
    onClick: () => void;
}
