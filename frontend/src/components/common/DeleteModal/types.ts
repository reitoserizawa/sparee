export type DeleteModalProps = {
    open: boolean;
    title?: string;
    description?: string;
    confirmText?: string;
    loading?: boolean;
    onClose: () => void;
    onConfirm: () => void;
};
