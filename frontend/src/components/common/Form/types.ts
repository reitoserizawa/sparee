import type { ReactNode } from 'react';

export type Validator<State> = (value: Partial<State>) => string[];

export interface FormState<State> {
    data: State;
    validators: Partial<Record<keyof State, Validator<State>[]>>;
    errors: Partial<Record<keyof State, string[]>>;
}

export interface FormContextType<State> {
    formState: FormState<State>;
    registerInput: (params: { name: keyof State; validators?: Validator<State>[] }) => () => void;
    handleChange: (e: React.ChangeEvent<HTMLInputElement>) => void;
}

export interface FormProviderProps<State> {
    children: ReactNode;
    initialValues: State;
    onSubmit: (data: State) => void;
    className?: string;
}

export interface FormInputProps<State> {
    name: keyof State;
    validators: Validator<State>[];
    placeholder?: string;
    type: string;
    label?: string;
}
