import { useEffect, useRef } from 'react';
import { useStateContext } from './formContext';
import getNestedValue from '../../../utils/getNestedValue';
import type { DotPaths, FormTextareaProps } from './types';
import Error from '../Error';

const FormTextarea = <State,>({
    name,
    validators,
    label,
    className,
    placeholder,
    rows = 4,
}: FormTextareaProps<State>) => {
    const { formState, registerInput, handleTextareaChange } = useStateContext<State>();
    const validatorsRef = useRef(validators);

    useEffect(() => {
        const unregister = registerInput({ name: name as DotPaths<State>, validators: validatorsRef.current });
        return unregister;
    }, [name, registerInput]);

    const { data, errors } = formState;
    const value = (getNestedValue(data, name) as string) ?? '';

    return (
        <>
            {label && <label className='block text-xs font-medium text-gray-500 mb-1'>{label}</label>}
            <textarea
                name={name}
                value={value}
                rows={rows}
                placeholder={placeholder}
                onChange={e => handleTextareaChange(e)}
                className={
                    className ??
                    'w-full rounded-lg border border-gray-300 px-3 py-2 text-sm focus:outline-none focus:ring-1 focus:ring-black resize-none'
                }
            />
            {errors[name]?.map((error, i) => (
                <Error key={i} message={error} />
            ))}
        </>
    );
};

export default FormTextarea;
