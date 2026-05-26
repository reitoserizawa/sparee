import type { Message } from '../../../store/features/chat/types';

export interface ChatBubbleProps {
    message: Message;
    isOwn: boolean;
}
