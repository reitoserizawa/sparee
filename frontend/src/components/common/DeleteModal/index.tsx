import React from 'react';
import Modal from '../../ui/Modal';
import Button from '../../ui/Button';
import type { DeleteModalProps } from './types';

const DeleteModal: React.FC<DeleteModalProps> = ({
    open,
    title = 'Delete item',
    description = 'Are you sure you want to delete this?',
    confirmText = 'Delete',
    loading = false,
    onClose,
    onConfirm,
}): React.ReactElement => {
    return (
        <Modal open={open} title={title} onClose={onClose}>
            <p className='text-sm text-gray-500 mb-6'>{description}</p>

            <div className='flex justify-end gap-3'>
                <Button variant='secondary' className='px-4 py-2 rounded-full text-sm' onClick={onClose}>
                    Cancel
                </Button>

                <Button
                    variant='danger'
                    className='px-4 py-2 rounded-full text-sm'
                    onClick={onConfirm}
                    disabled={loading}
                >
                    {loading ? 'Deleting...' : confirmText}
                </Button>
            </div>
        </Modal>
    );
};

export default DeleteModal;
