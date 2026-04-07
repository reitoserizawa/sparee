import getNestedValue from '../../../../utils/getNestedValue';
import type { Validator } from '../types';

const emailValidator = <State extends { email: string }>(): Validator<State> => {
    return (data: Partial<State>, name) => {
        const value = getNestedValue(data, name as string);
        if (value) {
            if (typeof value !== 'string') return ['Invalid value type'];

            const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            if (!regex.test(value)) return ['Invalid email format'];
        }

        return [];
    };
};

export default emailValidator;
