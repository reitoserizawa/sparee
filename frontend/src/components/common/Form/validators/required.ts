import type { Validator } from '../types';

const requiredValidator = <State>(): Validator<State> => {
    return value => {
        if (value) return [];

        return ['This field is required'];
    };
};

export default requiredValidator;
