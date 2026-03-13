type ButtonVariant = 'primary' | 'secondary' | 'ghost' | 'danger' | 'link' | 'brand';

export type ButtonProps = {
    children: React.ReactNode;
    type?: 'button' | 'submit' | 'reset';
    size?: 'sm' | 'md' | 'lg';
    variant?: ButtonVariant;
    disabled?: boolean;
    className?: string;
    onClick?: () => void;
};
