import getNestedValue from '../../../../utils/getNestedValue';
import type { Validator } from '../types';

const requiredValidator = <State>(): Validator<State> => {
    return (data, name) => {
        const value = getNestedValue(data, name as string);
        if (value) return [];
        return ['This field is required'];
    };
};

export default requiredValidator;
