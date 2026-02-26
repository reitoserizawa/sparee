import React from 'react';
import { useNavigate } from 'react-router-dom';

import { useLoginMutation } from '../../features/auth/authApi';
import { isErrorWithMessage } from '../../services/helpers';
import requiredValidator from '../common/Form/validators/required';
import emailValidator from '../common/Form/validators/email_validator';

import type { UserLoginFormState } from '../../types/user';

import Form from '../common/Form';
import FormInput from '../common/Form/FormInput';
import Error from '../common/Error';

const LoginPage = (): React.ReactElement => {
    const initialValues: UserLoginFormState = { email: '', password: '' };
    const navigate = useNavigate();
    const [login, { isLoading, isError, error }] = useLoginMutation();

    const handleSubmit = async (data: UserLoginFormState) => {
        try {
            await login(data).unwrap();
            navigate('/');
        } catch (err) {
            console.log(err);
        }
    };

    return (
        <div className='min-h-screen flex items-center justify-center bg-gray-50 px-4'>
            <div className='w-full max-w-md bg-white shadow-lg rounded-2xl p-8'>
                <div className='mb-6 text-center'>
                    <h1 className='text-2xl font-semibold tracking-tight'>Welcome back</h1>
                    <p className='text-sm text-gray-500 mt-1'>Sign in to your account</p>
                </div>
                <Form<UserLoginFormState> initialValues={initialValues} onSubmit={handleSubmit} className='space-y-4'>
                    <FormInput<UserLoginFormState>
                        name='email'
                        label='Email*'
                        type='text'
                        validators={[requiredValidator(), emailValidator()]}
                    />
                    <FormInput<UserLoginFormState>
                        name='password'
                        label='Password*'
                        type='password'
                        validators={[requiredValidator()]}
                    />
                    {isError && isErrorWithMessage(error) && <Error message={error?.data?.message} />}
                    <button
                        type='submit'
                        disabled={isLoading}
                        className='w-full rounded-lg bg-black text-white py-2 text-sm font-medium hover:opacity-90 disabled:opacity-50'
                    >
                        {isLoading ? 'Signing in...' : 'Sign in'}
                    </button>
                </Form>

                <p className='text-sm text-center text-gray-500 mt-6'>
                    Don’t have an account?{' '}
                    <a href='/register' className='text-black font-medium hover:underline'>
                        Sign up
                    </a>
                </p>
            </div>
        </div>
    );
};

export default LoginPage;
