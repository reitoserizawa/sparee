import type { Validator } from '../types';

const emailValidator = <State extends { email: string }>(): Validator<State> => {
    return (data: Partial<State>) => {
        if (data.email) {
            if (typeof data.email !== 'string') return ['Invalid value type'];

            const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            if (!regex.test(data.email)) return ['Invalid email format'];
        }

        return [];
    };
};

export default emailValidator;
