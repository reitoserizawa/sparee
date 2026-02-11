import type { ReactNode } from 'react';

export interface FormState<State> {
    data: State;
    validators: { [key in keyof State]?: ((value: unknown, data: Partial<State>) => string[])[] };
    errors: { [key in keyof State]?: string[] };
}

export interface FormContextType<State> {
    formState: FormState<State>;
    registerInput: ({
        name,
        validators,
    }: {
        name: keyof State;
        validators?: ((value: unknown, data: Partial<State>) => string[])[];
    }) => () => void;
    handleChange: (e: React.ChangeEvent<HTMLInputElement>) => void;
    handleDateChange: (name: keyof State, date: Date | null) => void;
}

export interface FormProviderProps<State> {
    children: ReactNode;
    initialValues?: State;
    onSubmit: (data: State) => void;
    className?: string;
}

export interface FormInputProps<State> {
    name: keyof State;
    validators?: ((value: unknown, data: Partial<unknown>) => string[])[];
    placeholder?: string;
    type?: string;
    label?: string;
}
