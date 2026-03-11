import type { CardProps } from './type';

const Card: React.FC<CardProps> = ({ children, className }) => {
    return <div className={`bg-white rounded-2xl p-6 shadow-sm ${className || ''}`}>{children}</div>;
};

export default Card;
