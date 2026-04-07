import { createContext, useContext } from 'react';
import type { FormContextType } from './types';

// eslint-disable-next-line @typescript-eslint/no-explicit-any
export const FormContext = createContext<FormContextType<any> | null>(null);

export const useStateContext = <State>() => {
    const context = useContext(FormContext);
    if (!context) throw new Error('useStateContext must be used inside Form');
    return context as FormContextType<State>;
};
