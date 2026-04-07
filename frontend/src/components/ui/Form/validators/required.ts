import type { Validator } from '../types';

const requiredValidator = <State>(): Validator<State> => {
    return (data, name) => {
        const value = data[name];
        if (value) return [];
        return ['This field is required'];
    };
};

export default requiredValidator;
