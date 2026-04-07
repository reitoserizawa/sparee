import React from 'react';
import { Link, useNavigate } from 'react-router-dom';

import { useRegisterMutation } from '../../store/features/auth/authApi';
import requiredValidator from '../ui/Form/validators/required';
import emailValidator from '../ui/Form/validators/email_validator';
import passwordMatchValidator from '../ui/Form/validators/password_validator';
import { isErrorWithMessage } from '../../store/features/base/helpers';

import type { UserCreateState } from '../../store/features/auth/types';

import Form from '../ui/Form';
import FormInput from '../ui/Form/FormInput';
import Error from '../ui/Error';
import Button from '../ui/Button';

const RegisterPage = (): React.ReactElement => {
    const initialValues: UserCreateState = {
        username: '',
        email: '',
        password: '',
        confirm_password: '',
    };
    const navigate = useNavigate();
    const [register, { isLoading, isError, error }] = useRegisterMutation();

    const handleSubmit = async (data: UserCreateState) => {
        try {
            await register(data).unwrap();
            navigate('/');
        } catch (err) {
            console.error('Failed to register user:', err);
        }
    };

    return (
        <div className='min-h-screen flex items-center justify-center bg-gray-50 px-4'>
            <div className='w-full max-w-md bg-white shadow-lg rounded-2xl p-8'>
                <div className='mb-6 text-center'>
                    <h1 className='text-2xl font-semibold tracking-tight'>Create an account</h1>
                    <p className='text-sm text-gray-500 mt-1'>Sign up to get started</p>
                </div>

                <Form<UserCreateState> initialValues={initialValues} onSubmit={handleSubmit} className='space-y-4'>
                    <FormInput<UserCreateState>
                        name='username'
                        label='Username*'
                        type='text'
                        validators={[requiredValidator()]}
                    />
                    <FormInput<UserCreateState>
                        name='email'
                        label='Email*'
                        type='text'
                        validators={[requiredValidator(), emailValidator()]}
                    />
                    <FormInput<UserCreateState>
                        name='password'
                        label='Password*'
                        type='password'
                        validators={[requiredValidator()]}
                    />
                    <FormInput<UserCreateState>
                        name='confirm_password'
                        label='Confirm Password*'
                        type='password'
                        validators={[requiredValidator(), passwordMatchValidator()]}
                    />
                    {isError && isErrorWithMessage(error) && <Error message={error?.data?.message} />}
                    <Button type='submit' disabled={isLoading} className='w-full rounded-lg py-2 text-sm'>
                        {isLoading ? 'Creating account...' : 'Sign in'}
                    </Button>
                </Form>

                <p className='text-sm text-center text-gray-500 mt-6'>
                    Already have an account?{' '}
                    <Link to='/login' className='text-black font-medium hover:underline'>
                        Sign in
                    </Link>
                </p>
            </div>
        </div>
    );
};

export default RegisterPage;
