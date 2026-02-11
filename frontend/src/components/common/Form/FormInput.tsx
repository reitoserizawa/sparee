import React, { useEffect } from 'react';
import { useStateContext } from './formContext';
import type { FormInputProps } from './types';

import Error from '../Error';

const FormInput = <State,>({ name, validators, placeholder, label, type = 'text' }: FormInputProps<State>) => {
    const { formState, registerInput, handleChange } = useStateContext<State>();

    useEffect(() => {
        const unregister = registerInput({ name, validators });
        return unregister;
    }, [name, validators, registerInput]);

    const { data, errors } = formState;

    return (
        <>
            {label ? <p>{label}</p> : null}
            <input
                name={name as string}
                value={data[name] ? (data[name] as string) : ''}
                onChange={e => handleChange(e)}
                placeholder={placeholder}
                type={type}
            />
            {errors[name] && errors[name]?.map((error, i) => <Error key={i} message={error} />)}
        </>
    );
};

export default FormInput;
