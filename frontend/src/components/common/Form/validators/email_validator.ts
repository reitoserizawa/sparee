import type { Validator } from '../types';

export const emailValidator = <State>(): Validator<State> => {
    return value => {
        if (typeof value !== 'string') return ['Invalid value type'];

        const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!regex.test(value)) return ['Invalid email format'];

        return [];
    };
};
