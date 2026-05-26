import React from 'react';
import type { ChatBubbleProps } from './types';
import { format } from 'date-fns';

const ChatBubble: React.FC<ChatBubbleProps> = ({ message, isOwn }) => {
    return (
        <div className={`flex ${isOwn ? 'justify-end' : 'justify-start'}`}>
            <div
                className={`max-w-xs lg:max-w-md xl:max-w-lg ${isOwn ? 'items-end' : 'items-start'} flex flex-col gap-1`}
            >
                <div
                    className={`px-4 py-2.5 rounded-2xl text-sm leading-relaxed ${
                        isOwn
                            ? 'bg-blue-600 text-white rounded-br-md'
                            : 'bg-white text-gray-800 rounded-bl-md shadow-sm border border-gray-100'
                    }`}
                >
                    {message.body}
                </div>
                <span className='text-xs text-gray-400 px-1'>
                    {format(new Date(message.timestamp), 'h:mm a')}
                    {isOwn && <span className='ml-1 text-blue-400'>{message.is_read ? '✓✓' : '✓'}</span>}
                </span>
            </div>
        </div>
    );
};

export default ChatBubble;
