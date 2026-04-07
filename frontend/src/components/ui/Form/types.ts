import type { ReactNode } from 'react';

// accept nested paths
export type DotPaths<T> = T extends object
    ? {
          [K in keyof T & string]: T[K] extends object ? `${K}.${DotPaths<T[K]>}` | K : K;
      }[keyof T & string]
    : string;

export type Validator<State> = (value: State, name: keyof State) => string[];

export interface FormState<State> {
    data: State;
    validators: Partial<Record<string, Validator<State>[]>>;
    errors: Partial<Record<string, string[]>>;
}

export interface FormContextType<State> {
    formState: FormState<State>;
    registerInput: (params: { name: string; validators?: Validator<State>[] }) => () => void;
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
