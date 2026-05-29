import React, { useState } from 'react';
import type { StatusDropdownProps } from './types';
import { STATUS_CONFIG, STATUSES } from '../../../constants/STATUS_COLORS';
import ChevronDownIcon from '../../../assets/icons/ChevronDownIcon';
import CheckIcon from '../../../assets/icons/CheckIcon';

const StatusDropdown: React.FC<StatusDropdownProps> = ({ current, onChange, isSaving }) => {
    const [open, setOpen] = useState(false);
    const cfg = STATUS_CONFIG[current];

    return (
        <div className='relative'>
            <button
                onClick={() => setOpen(o => !o)}
                disabled={isSaving}
                className={`inline-flex items-center gap-2 px-3 py-1.5 rounded-lg border text-sm font-medium transition-all
                    ${cfg.badge} hover:brightness-95 disabled:opacity-60`}
            >
                {isSaving ? (
                    <span className='w-3 h-3 border-2 border-current/30 border-t-current rounded-full animate-spin' />
                ) : (
                    <span className={`w-2 h-2 rounded-full flex-shrink-0 ${cfg.dot}`} />
                )}
                {cfg.label}
                <ChevronDownIcon className={`w-3.5 h-3.5 transition-transform ${open ? 'rotate-180' : ''}`} />
            </button>

            {open && (
                <>
                    <div className='fixed inset-0 z-10' onClick={() => setOpen(false)} />
                    <div
                        className='absolute left-0 top-full mt-1.5 z-20 bg-white rounded-xl border border-gray-200 shadow-lg overflow-hidden min-w-[160px]'
                        onClick={e => e.stopPropagation()} // prevents backdrop from closing before onChange fires
                    >
                        {STATUSES.filter(status => status !== current && status !== 'withdrawn').map(status => {
                            const c = STATUS_CONFIG[status];
                            const isActive = status === current;
                            return (
                                <button
                                    key={status}
                                    onClick={() => {
                                        onChange(status);
                                        setOpen(false);
                                    }}
                                    className='w-full flex items-center gap-2.5 px-3.5 py-2.5 text-sm text-left hover:bg-gray-50 transition-colors'
                                >
                                    <span className={`w-2 h-2 rounded-full flex-shrink-0 ${c.dot}`} />
                                    <span className={isActive ? 'font-semibold text-gray-900' : 'text-gray-600'}>
                                        {c.label}
                                    </span>
                                    {isActive && <CheckIcon className='w-3.5 h-3.5 text-gray-400 ml-auto' />}
                                </button>
                            );
                        })}
                    </div>
                </>
            )}
        </div>
    );
};

export default StatusDropdown;
