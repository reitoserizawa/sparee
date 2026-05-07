import React, { useState } from 'react';
import type { EditStatusModalProps } from './types';
import type { JobApplicationStatus } from '../../../store/features/jobApplication/types';
import { STATUS_CONFIG, STATUSES } from '../../../constants/STATUS_COLORS';

const EditStatusModal: React.FC<EditStatusModalProps> = ({ open, application, onClose, onSave, isSaving }) => {
    const [selected, setSelected] = useState<JobApplicationStatus>(application.application_status);

    if (!open || !application) return null;

    const handleSave = async () => {
        await onSave(application.id, selected);
        onClose();
    };

    return (
        <div className='fixed inset-0 z-50 flex items-center justify-center'>
            {/* Backdrop */}
            <div className='absolute inset-0 bg-black/40 backdrop-blur-[2px] transition-opacity' onClick={onClose} />

            {/* Panel */}
            <div className='relative z-10 w-full max-w-sm mx-4 bg-white rounded-2xl shadow-2xl overflow-hidden'>
                {/* Header strip */}
                <div className='h-1 bg-gradient-to-r from-indigo-500 via-violet-500 to-purple-500' />

                <div className='p-6'>
                    <div className='mb-1 text-xs font-semibold tracking-widest text-gray-400 uppercase'>
                        Update Status
                    </div>
                    <h2 className='text-base font-semibold text-gray-900 mb-1 truncate'>
                        {application.job_post.title}
                    </h2>
                    <p className='text-xs text-gray-500 mb-5'>
                        Application #{application.id} · {application.user.username}
                    </p>

                    {/* Status options */}
                    <div className='grid grid-cols-2 gap-2 mb-6'>
                        {STATUSES.map(status => {
                            const cfg = STATUS_CONFIG[status];
                            const isSelected = selected === status;
                            return (
                                <button
                                    key={status}
                                    onClick={() => setSelected(status)}
                                    className={`flex items-center gap-2.5 px-3.5 py-2.5 rounded-xl border-2 text-left text-sm font-medium transition-all duration-150
                                        ${
                                            isSelected
                                                ? `border-transparent ring-2 ${cfg.ring} ${cfg.badge}`
                                                : 'border-gray-200 text-gray-600 hover:border-gray-300 hover:bg-gray-50'
                                        }`}
                                >
                                    <span
                                        className={`w-2 h-2 rounded-full flex-shrink-0 ${isSelected ? cfg.dot : 'bg-gray-300'}`}
                                    />
                                    {cfg.label}
                                </button>
                            );
                        })}
                    </div>

                    {/* Actions */}
                    <div className='flex gap-2'>
                        <button
                            onClick={onClose}
                            disabled={isSaving}
                            className='flex-1 px-4 py-2 rounded-xl border border-gray-200 text-sm font-medium text-gray-600 hover:bg-gray-50 transition-colors disabled:opacity-50'
                        >
                            Cancel
                        </button>
                        <button
                            onClick={handleSave}
                            disabled={isSaving || selected === application.application_status}
                            className='flex-1 px-4 py-2 rounded-xl bg-gray-900 text-sm font-medium text-white hover:bg-gray-700 transition-colors disabled:opacity-40 flex items-center justify-center gap-2'
                        >
                            {isSaving ? (
                                <>
                                    <span className='w-3.5 h-3.5 border-2 border-white/30 border-t-white rounded-full animate-spin' />
                                    Saving…
                                </>
                            ) : (
                                'Save'
                            )}
                        </button>
                    </div>
                </div>
            </div>
        </div>
    );
};

export default EditStatusModal;
