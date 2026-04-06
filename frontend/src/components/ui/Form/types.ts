import type { ReactNode } from 'react';

// accept nested paths
export type DotPaths<T, Prefix extends string = ''> = {
    [K in keyof T & string]: T[K] extends object ? DotPaths<T[K], `${Prefix}${K}.`> | `${Prefix}${K}` : `${Prefix}${K}`;
}[keyof T & string];

export type Validator<State> = (value: Partial<State>) => string[];

export interface FormState<State> {
    data: State;
    validators: Partial<Record<string, Validator<State>[]>>;
    errors: Partial<Record<string, string[]>>;
}

export interface FormContextType<State> {
    formState: FormState<State>;
    registerInput: (params: { name: DotPaths<State>; validators?: Validator<State>[] }) => () => void;
    handleChange: (e: React.ChangeEvent<HTMLInputElement>) => void;
}

export interface FormProviderProps<State> {
    children: ReactNode;
    initialValues: State;
    onSubmit: (data: State) => void;
    className?: string;
}

export interface FormInputProps<State> {
    name: DotPaths<State>;
    validators: Validator<State>[];
    placeholder?: string;
    type: string;
    label?: string;
}
