import type { Validator } from '../types';

const emailValidator = <State>(): Validator<State> => {
    return value => {
        if (typeof value !== 'string') return ['Invalid value type'];

        const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!regex.test(value)) return ['Invalid email format'];

        return [];
    };
};

export default emailValidator;
