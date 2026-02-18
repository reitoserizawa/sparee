import React, { useState } from 'react';

import Form from '../common/Form';
import FormInput from '../common/Form/FormInput';
import type { UserLoginRequest } from '../../types/user';
import requiredValidator from '../common/Form/validators/required';
import { emailValidator } from '../common/Form/validators/email_validator';

const LoginPage = (): React.ReactElement => {
    const initialValues: UserLoginRequest = { email: '', password: '' };

    const [loading, setLoading] = useState(false);

    const handleSubmit = async (data: UserLoginRequest) => {
        setLoading(true);
        try {
            const response = await fetch(`${import.meta.env.VITE_API_URL}users/login`, {
                method: 'POST',
                credentials: 'include',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(data),
            });
            const responseData = await response.json();
            if (!response.ok) {
                throw new Error(responseData.detail || 'Login failed');
            }
            console.log('Login successful:', responseData);
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className='min-h-screen flex items-center justify-center bg-gray-50 px-4'>
            <div className='w-full max-w-md bg-white shadow-lg rounded-2xl p-8'>
                <div className='mb-6 text-center'>
                    <h1 className='text-2xl font-semibold tracking-tight'>Welcome back</h1>
                    <p className='text-sm text-gray-500 mt-1'>Sign in to your account</p>
                </div>
                <Form<UserLoginRequest> initialValues={initialValues} onSubmit={handleSubmit} className='space-y-4'>
                    <FormInput<UserLoginRequest> name='email' label='Email*' type='text' validators={[requiredValidator(), emailValidator()]} />
                    <FormInput<UserLoginRequest> name='password' label='Password*' type='password' validators={[requiredValidator()]} />
                    <button
                        type='submit'
                        disabled={loading}
                        className='w-full rounded-lg bg-black text-white py-2 text-sm font-medium hover:opacity-90 disabled:opacity-50'
                    >
                        {loading ? 'Signing in...' : 'Sign in'}
                    </button>
                </Form>

                <p className='text-sm text-center text-gray-500 mt-6'>
                    Don’t have an account?{' '}
                    <a href='#' className='text-black font-medium hover:underline'>
                        Sign up
                    </a>
                </p>
            </div>
        </div>
    );
};

export default LoginPage;
