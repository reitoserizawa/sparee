import React, { useState, useCallback } from 'react';
import { FormContext } from './formContext';
import type { FormProviderProps, FormState, Validator } from './types';

const setNestedValue = <State,>(obj: State, path: string, value: string): State => {
    const keys = path.split('.');
    const lastKey = keys.pop()!;
    const newObj = { ...(obj as object) } as State;
    // eslint-disable-next-line @typescript-eslint/no-explicit-any
    let curr: any = newObj;
    for (const key of keys) {
        curr[key] = { ...curr[key] };
        curr = curr[key];
    }
    curr[lastKey] = value;
    return newObj;
};

const Form = <State,>({ children, initialValues, onSubmit, className }: FormProviderProps<State>) => {
    const [formState, setFormState] = useState<FormState<State>>({
        data: initialValues ?? ({} as State),
        validators: {},
        errors: {},
    });

    const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
        const { name, value } = e.target;
        setFormState(prev => ({
            ...prev,
            data: setNestedValue(prev.data, name, value),
        }));
    };

    const registerInput = useCallback(({ name, validators }: { name: string; validators?: Validator<State>[] }) => {
        setFormState(prev => ({
            ...prev,
            validators: { ...prev.validators, [name]: validators || [] },
            errors: { ...prev.errors, [name]: [] },
        }));

        return () => {
            setFormState(prev => {
                const restErrors = { ...prev.errors };
                delete restErrors[name];
                const restValidators = { ...prev.validators };
                delete restValidators[name];
                return { ...prev, errors: restErrors, validators: restValidators };
            });
        };
    }, []);

    const validate = (): boolean => {
        const newErrors: Partial<Record<string, string[]>> = {};

        Object.keys(formState.validators).forEach(name => {
            const fieldValidators = formState.validators[name];
            if (!fieldValidators) return;
            const messages = fieldValidators.flatMap(v => v(formState.data as State, name as keyof State));
            if (messages.length) newErrors[name] = messages;
        });

        if (Object.keys(newErrors).length) {
            setFormState(prev => ({ ...prev, errors: newErrors }));
            return false;
        }
        return true;
    };

    const onSubmitHandler = (e: React.FormEvent) => {
        e.preventDefault();

        if (validate()) {
            onSubmit(formState.data);
        }
    };

    return (
        <FormContext.Provider value={{ formState, registerInput, handleChange }}>
            <form onSubmit={onSubmitHandler} className={className}>
                {children}
            </form>
        </FormContext.Provider>
    );
};

export default Form;
