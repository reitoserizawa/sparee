import React, { useState } from 'react';

type FormState = {
    email: string;
    password: string;
};

export default function LoginPage() {
    const [form, setForm] = useState<FormState>({ email: '', password: '' });
    const [loading, setLoading] = useState(false);

    const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
        setForm({ ...form, [e.target.name]: e.target.value });
    };

    const handleSubmit = async (e: React.FormEvent) => {
        e.preventDefault();
        setLoading(true);

        try {
            // 👉 replace with real API call
            await new Promise(r => setTimeout(r, 1000));
            alert(JSON.stringify(form, null, 2));
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

                <form onSubmit={handleSubmit} className='space-y-4'>
                    <div>
                        <label className='block text-sm font-medium mb-1'>Email</label>
                        <input
                            name='email'
                            type='email'
                            required
                            value={form.email}
                            onChange={handleChange}
                            className='w-full rounded-lg border border-gray-300 px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-black'
                            placeholder='you@example.com'
                        />
                    </div>

                    <div>
                        <div className='flex items-center justify-between mb-1'>
                            <label className='text-sm font-medium'>Password</label>
                            <button type='button' className='text-xs text-gray-500 hover:text-black'>
                                Forgot?
                            </button>
                        </div>
                        <input
                            name='password'
                            type='password'
                            required
                            value={form.password}
                            onChange={handleChange}
                            className='w-full rounded-lg border border-gray-300 px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-black'
                            placeholder='••••••••'
                        />
                    </div>

                    <button
                        type='submit'
                        disabled={loading}
                        className='w-full rounded-lg bg-black text-white py-2 text-sm font-medium hover:opacity-90 disabled:opacity-50'
                    >
                        {loading ? 'Signing in...' : 'Sign in'}
                    </button>
                </form>

                <p className='text-sm text-center text-gray-500 mt-6'>
                    Don’t have an account?{' '}
                    <a href='#' className='text-black font-medium hover:underline'>
                        Sign up
                    </a>
                </p>
            </div>
        </div>
    );
}
