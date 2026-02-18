import React, { useState, useCallback } from 'react';
import { FormContext } from './formContext';
import type { FormProviderProps, FormState } from './types';

const Form = <State,>({ children, initialValues, onSubmit, className }: FormProviderProps<State>) => {
    const [formState, setFormState] = useState<FormState<State>>({
        data: initialValues ?? ({} as State),
        validators: {},
        errors: {},
    });

    const updateField = (name: keyof State, value: string) => {
        setFormState(prev => ({
            ...prev,
            data: {
                ...prev.data,
                [name]: value,
            },
        }));
    };

    const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
        updateField(e.target.name as keyof State, e.target.value);
    };

    const registerInput = useCallback(({ name, validators }: { name: keyof State; validators?: ((value: Partial<State>) => string[])[] }) => {
        setFormState(prev => ({
            ...prev,
            validators: {
                ...prev?.validators,
                [name]: validators || [],
            },
            errors: {
                ...prev.errors,
                [name]: [],
            },
        }));

        return () => {
            setFormState(prev => {
                const restErrors = { ...prev.errors };
                delete restErrors[name];

                const restValidators = { ...prev.validators };
                delete restValidators[name];
                return {
                    ...prev,
                    errors: restErrors,
                    validators: restValidators,
                };
            });
        };
    }, []);

    const validate = (): boolean => {
        const newErrors: Partial<Record<keyof State, string[]>> = {};

        (Object.keys(formState.validators) as (keyof State)[]).forEach(name => {
            const fieldValidators = formState.validators[name];
            if (!fieldValidators) return;

            const value = formState.data[name] as Partial<State>;
            const messages = fieldValidators.flatMap(validator => validator(value));

            if (messages.length) {
                newErrors[name] = messages;
            }
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
