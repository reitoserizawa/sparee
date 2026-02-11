import React, { useContext } from 'react';
import type { FormContextType } from './types';

export const FormContext = React.createContext<FormContextType<unknown> | null>(null);

export const useStateContext = <State>() => {
    const context = useContext(FormContext);
    if (!context) throw new Error('useStateContext must be used inside Form');
    return context as FormContextType<State>;
};
