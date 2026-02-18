import { useEffect } from 'react';
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
            {label ? <label className='block text-sm font-medium mb-1'>{label}</label> : null}
            <input
                name={name as string}
                value={data[name] ? (data[name] as string) : ''}
                onChange={e => handleChange(e)}
                placeholder={placeholder}
                type={type}
                className='w-full rounded-lg border border-gray-300 px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-black'
            />
            {errors[name] && errors[name]?.map((error, i) => <Error key={i} message={error} />)}
        </>
    );
};

export default FormInput;
