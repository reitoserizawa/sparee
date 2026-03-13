import React from 'react';
import { Link, useNavigate } from 'react-router-dom';

import { useLoginMutation } from '../../store/features/auth/authApi';
import { isErrorWithMessage } from '../../store/features/base/helpers';
import requiredValidator from '../ui/Form/validators/required';
import emailValidator from '../ui/Form/validators/email_validator';

import type { UserLoginState } from '../../store/features/auth/types';

import Form from '../ui/Form';
import FormInput from '../ui/Form/FormInput';
import Error from '../ui/Error';
import Button from '../ui/Button';

const LoginPage = (): React.ReactElement => {
    const initialValues: UserLoginState = { email: '', password: '' };
    const navigate = useNavigate();
    const [login, { isLoading, isError, error }] = useLoginMutation();

    const handleSubmit = async (data: UserLoginState) => {
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
                <Form<UserLoginState> initialValues={initialValues} onSubmit={handleSubmit} className='space-y-4'>
                    <FormInput<UserLoginState>
                        name='email'
                        label='Email*'
                        type='text'
                        validators={[requiredValidator(), emailValidator()]}
                    />
                    <FormInput<UserLoginState>
                        name='password'
                        label='Password*'
                        type='password'
                        validators={[requiredValidator()]}
                    />
                    {isError && isErrorWithMessage(error) && <Error message={error?.data?.message} />}
                    <Button type='submit' disabled={isLoading} className='w-full rounded-lg py-2 text-sm'>
                        {isLoading ? 'Signing in...' : 'Sign in'}
                    </Button>
                </Form>

                <p className='text-sm text-center text-gray-500 mt-6'>
                    Don’t have an account?{' '}
                    <Link to='/register' className='text-black font-medium hover:underline'>
                        Sign up
                    </Link>
                </p>
            </div>
        </div>
    );
};

export default LoginPage;
