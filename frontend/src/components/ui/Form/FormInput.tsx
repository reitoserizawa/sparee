import { useEffect, useRef } from 'react';
import { useStateContext } from './formContext';
import getNestedValue from '../../../utils/getNestedValue';
import type { DotPaths, FormInputProps } from './types';

import Error from '../Error';

const FormInput = <State,>({
    name,
    validators,
    placeholder,
    label,
    className,
    type = 'text',
}: FormInputProps<State>) => {
    const { formState, registerInput, handleChange } = useStateContext<State>();
    const validatorsRef = useRef(validators);

    useEffect(() => {
        const unregister = registerInput({ name: name as DotPaths<State>, validators: validatorsRef.current });
        return unregister;
    }, [name, registerInput]);

    const { data, errors } = formState;
    const value = (getNestedValue(data, name) as string) ?? '';

    return (
        <>
            {label && <label className='block text-sm font-medium text-gray-500 mb-1'>{label}</label>}
            <input
                name={name}
                value={value}
                onChange={e => handleChange(e)}
                placeholder={placeholder}
                type={type}
                className={
                    className ??
                    'w-full rounded-lg border border-gray-300 px-3 py-2 text-sm focus:outline-none focus:ring-1 focus:ring-black bg-white'
                }
            />
            {errors[name]?.map((error, i) => (
                <Error key={i} message={error} />
            ))}
        </>
    );
};

export default FormInput;
