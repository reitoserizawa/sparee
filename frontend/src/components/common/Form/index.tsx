import React, { useState, useCallback } from 'react';
import { FormContext } from './formContext';
import type { FormProviderProps, FormState } from './types';

const Form = <State,>({ children, initialValues, onSubmit, className }: FormProviderProps<State>) => {
    const [formState, setFormState] = useState<FormState<State>>({
        data: initialValues || ({} as State),
        validators: {},
        errors: {},
    });

    const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
        const { name, value } = e.target;

        setFormState(prevValues => ({
            ...prevValues,
            data: {
                ...prevValues.data,
                [name as keyof State]: value,
            },
        }));
    };

    const handleDateChange = (name: keyof State, date: Date | null) => {
        setFormState(prevValues => ({
            ...prevValues,
            data: {
                ...prevValues.data,
                [name as keyof State]: date,
            },
        }));
    };

    const registerInput = useCallback(
        ({
            name,
            validators,
        }: {
            name: keyof State;
            validators?: ((value: unknown, data: Partial<State>) => string[])[];
        }) => {
            setFormState(state => ({
                ...state,
                validators: {
                    ...state.validators,
                    [name]: validators || [],
                },
                errors: {
                    ...state.errors,
                    [name]: [],
                },
            }));

            return () => {
                setFormState(state => {
                    const { data, errors, validators: currentValidators } = { ...state };
                    delete data[name];
                    delete errors[name];
                    delete currentValidators[name];
                    return {
                        data,
                        errors,
                        validators: currentValidators,
                    };
                });
            };
        },
        [],
    );

    const validate = (): boolean => {
        const { validators, data } = formState;

        if (!validators || Object.keys(validators).length === 0) return true;

        const formErrors = Object.entries(validators).reduce(
            (errors, [name, fieldValidators]) => {
                if (!Array.isArray(fieldValidators)) return errors;

                const messages = fieldValidators.reduce<string[]>((result, validator) => {
                    const value = data[name as keyof typeof data];
                    const err = validator(value, data);
                    return [...result, ...err];
                }, []);
                if (messages.length > 0) errors[name] = messages;
                return errors;
            },
            {} as Record<string, string[]>,
        );

        if (Object.keys(formErrors).length === 0) return true;

        setFormState(state => ({ ...state, errors: formErrors }));
        return false;
    };

    const onSubmitHandler = (e: React.FormEvent) => {
        e.preventDefault();

        if (validate()) {
            onSubmit(formState.data);
        }
    };

    return (
        <FormContext.Provider value={{ formState, registerInput, handleChange, handleDateChange }}>
            <form onSubmit={onSubmitHandler} className={className}>
                {children}
            </form>
        </FormContext.Provider>
    );
};

export default Form;
