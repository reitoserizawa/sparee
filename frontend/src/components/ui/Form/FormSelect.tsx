import { useEffect, useRef } from 'react';
import { useStateContext } from './formContext';
import getNestedValue from '../../../utils/getNestedValue';
import type { DotPaths, FormSelectProps } from './types';
import Error from '../Error';

const FormSelect = <State,>({
    name,
    validators,
    label,
    className,
    options,
    placeholder,
    disabled,
}: FormSelectProps<State>) => {
    const { formState, registerInput, handleSelectChange } = useStateContext<State>();
    const validatorsRef = useRef(validators);

    useEffect(() => {
        const unregister = registerInput({ name: name as DotPaths<State>, validators: validatorsRef.current });
        return unregister;
    }, [name, registerInput]);

    const { data, errors } = formState;
    const value = (getNestedValue(data, name) as string | number) ?? '';

    return (
        <>
            {label && <label className='block text-sm font-medium text-gray-500 mb-1'>{label}</label>}
            <select
                name={name}
                value={value}
                disabled={disabled}
                onChange={e => handleSelectChange(e)}
                className={
                    className ??
                    'w-full rounded-lg border border-gray-300 px-3 py-2 text-sm focus:outline-none focus:ring-1 focus:ring-black bg-white'
                }
            >
                {placeholder && <option value=''>{placeholder}</option>}
                {options.map(opt => (
                    <option key={opt.value} value={opt.value}>
                        {opt.label}
                    </option>
                ))}
            </select>
            {errors[name]?.map((error, i) => (
                <Error key={i} message={error} />
            ))}
        </>
    );
};

export default FormSelect;
