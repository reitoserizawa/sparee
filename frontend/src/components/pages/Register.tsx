import React from 'react';
import { Link, useNavigate } from 'react-router-dom';

import { useRegisterMutation } from '../../features/auth/authApi';
import requiredValidator from '../common/Form/validators/required';
import emailValidator from '../common/Form/validators/email_validator';
import { isErrorWithMessage } from '../../services/helpers';

import type { UserCreateFormState } from '../../types/user';

import Form from '../common/Form';
import FormInput from '../common/Form/FormInput';
import Error from '../common/Error';

const RegisterPage = (): React.ReactElement => {
    const initialValues: UserCreateFormState = {
        name: '',
        email: '',
        password: '',
        confirmPassword: '',
    };
    const navigate = useNavigate();
    const [register, { isSuccess, isLoading, isError, error }] = useRegisterMutation();

    const handleSubmit = async (data: UserCreateFormState) => {
        await register(data);
        if (isSuccess) {
            navigate('/');
        }
    };

    return (
        <div className='min-h-screen flex items-center justify-center bg-gray-50 px-4'>
            <div className='w-full max-w-md bg-white shadow-lg rounded-2xl p-8'>
                <div className='mb-6 text-center'>
                    <h1 className='text-2xl font-semibold tracking-tight'>Create an account</h1>
                    <p className='text-sm text-gray-500 mt-1'>Sign up to get started</p>
                </div>

                <Form<UserCreateFormState> initialValues={initialValues} onSubmit={handleSubmit} className='space-y-4'>
                    <FormInput<UserCreateFormState>
                        name='name'
                        label='Name*'
                        type='text'
                        validators={[requiredValidator()]}
                    />
                    <FormInput<UserCreateFormState>
                        name='email'
                        label='Email*'
                        type='text'
                        validators={[requiredValidator(), emailValidator()]}
                    />
                    <FormInput<UserCreateFormState>
                        name='password'
                        label='Password*'
                        type='password'
                        validators={[requiredValidator()]}
                    />
                    <FormInput<UserCreateFormState>
                        name='confirmPassword'
                        label='Confirm Password*'
                        type='password'
                        validators={[requiredValidator()]}
                    />
                    {isError && isErrorWithMessage(error) && <Error message={error?.data?.message} />}
                    <button
                        type='submit'
                        disabled={isLoading}
                        className='w-full rounded-lg bg-black text-white py-2 text-sm font-medium hover:opacity-90 disabled:opacity-50'
                    >
                        {isLoading ? 'Creating account...' : 'Sign in'}
                    </button>
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
