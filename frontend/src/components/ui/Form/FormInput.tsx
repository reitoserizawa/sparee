import { useEffect, useRef } from 'react';
import { useStateContext } from './formContext';
import type { DotPaths, FormInputProps } from './types';

import Error from '../Error';

// @typescript-eslint/no-explicit-any
const getNestedValue = (obj: unknown, path: string): unknown =>
    path.split('.').reduce((acc, key) => (acc as Record<string, unknown>)?.[key], obj);

const FormInput = <State,>({ name, validators, placeholder, label, type = 'text' }: FormInputProps<State>) => {
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
            {label ? <label className='block text-sm font-medium mb-1'>{label}</label> : null}
            <input
                name={name}
                value={value}
                onChange={e => handleChange(e)}
                placeholder={placeholder}
                type={type}
                className='w-full rounded-lg border border-gray-300 px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-black'
            />
            {errors[name]?.map((error, i) => (
                <Error key={i} message={error} />
            ))}
        </>
    );
};

export default FormInput;
