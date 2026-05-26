import React from 'react';
import { format } from 'date-fns';

import type { ConversationItemProps } from './types';
import Avatar from '../../ui/Avatar';
import { useAppSelector } from '../../../store/hooks';
import { selectCurrentUser } from '../../../store/features/auth/authSelector';

const ConversationItem: React.FC<ConversationItemProps> = ({ conversation, isActive, onClick }) => {
    const currentUser = useAppSelector(selectCurrentUser);

    // TODO: set it for a 1-1 message for now
    const { participants, messages, unread_count } = conversation;
    const lastMessage = messages[messages.length - 1];
    const isFromMe = lastMessage.sender_id === currentUser?.id;

    return (
        <button
            onClick={onClick}
            className={`w-full flex items-center gap-3 px-4 py-3 rounded-xl transition-colors text-left ${
                isActive ? 'bg-blue-50 border border-blue-100' : 'hover:bg-gray-50'
            }`}
        >
            <Avatar initial={participants[0].username[0]} isOnline={false} />
            <div className='flex-1 min-w-0'>
                <div className='flex items-center justify-between mb-0.5'>
                    <span className={`text-sm font-medium ${unread_count > 0 ? 'text-gray-900' : 'text-gray-700'}`}>
                        {participants[0].username}
                    </span>
                    <span className='text-xs text-gray-400 flex-shrink-0'>
                        {format(new Date(lastMessage.timestamp), 'MMM d')}
                    </span>
                </div>
                <div className='flex items-center justify-between gap-2'>
                    <p className='text-xs text-gray-500 truncate'>
                        {isFromMe ? 'You: ' : ''}
                        {lastMessage.body}
                    </p>
                    {unread_count > 0 && (
                        <span className='flex-shrink-0 h-5 w-5 rounded-full bg-blue-600 text-white text-xs flex items-center justify-center font-medium'>
                            {unread_count}
                        </span>
                    )}
                </div>
            </div>
        </button>
    );
};

export default ConversationItem;
