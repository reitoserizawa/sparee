import type { ReactNode } from 'react';

// accept nested paths
export type DotPaths<T> = T extends object
    ? {
          [K in keyof T & string]: NonNullable<T[K]> extends object ? `${K}.${DotPaths<NonNullable<T[K]>>}` | K : K;
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
    handleSelectChange: (e: React.ChangeEvent<HTMLSelectElement>) => void;
    handleTextareaChange: (e: React.ChangeEvent<HTMLTextAreaElement>) => void;
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
    className?: string;
}

export interface SelectOption {
    value: string | number;
    label: string;
}

export interface SelectOption {
    value: string | number;
    label: string;
}

export interface FormSelectProps<State> {
    name: DotPaths<State>;
    validators?: Validator<State>[];
    label?: string;
    className?: string;
    options: SelectOption[];
    placeholder?: string;
    disabled?: boolean;
}

export interface FormTextareaProps<State> {
    name: DotPaths<State>;
    validators?: Validator<State>[];
    label?: string;
    className?: string;
    placeholder?: string;
    rows?: number;
}
