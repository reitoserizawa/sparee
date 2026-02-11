import React, { useState } from 'react';

type FormState = {
    name: string;
    email: string;
    password: string;
    confirmPassword: string;
};

export default function SignUpPage() {
    const [form, setForm] = useState<FormState>({
        name: '',
        email: '',
        password: '',
        confirmPassword: '',
    });
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState<string | null>(null);

    const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
        setForm({ ...form, [e.target.name]: e.target.value });
    };

    const handleSubmit = async (e: React.FormEvent) => {
        e.preventDefault();
        setError(null);

        if (form.password !== form.confirmPassword) {
            setError('Passwords do not match');
            return;
        }

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
                    <h1 className='text-2xl font-semibold tracking-tight'>Create an account</h1>
                    <p className='text-sm text-gray-500 mt-1'>Sign up to get started</p>
                </div>

                <form onSubmit={handleSubmit} className='space-y-4'>
                    <div>
                        <label className='block text-sm font-medium mb-1'>Name</label>
                        <input
                            name='name'
                            type='text'
                            required
                            value={form.name}
                            onChange={handleChange}
                            className='w-full rounded-lg border border-gray-300 px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-black'
                            placeholder='Jane Doe'
                        />
                    </div>

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
                        <label className='block text-sm font-medium mb-1'>Password</label>
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

                    <div>
                        <label className='block text-sm font-medium mb-1'>Confirm Password</label>
                        <input
                            name='confirmPassword'
                            type='password'
                            required
                            value={form.confirmPassword}
                            onChange={handleChange}
                            className='w-full rounded-lg border border-gray-300 px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-black'
                            placeholder='••••••••'
                        />
                    </div>

                    {error && <p className='text-sm text-red-600'>{error}</p>}

                    <button
                        type='submit'
                        disabled={loading}
                        className='w-full rounded-lg bg-black text-white py-2 text-sm font-medium hover:opacity-90 disabled:opacity-50'
                    >
                        {loading ? 'Creating account...' : 'Sign up'}
                    </button>
                </form>

                <p className='text-sm text-center text-gray-500 mt-6'>
                    Already have an account?{' '}
                    <a href='#' className='text-black font-medium hover:underline'>
                        Sign in
                    </a>
                </p>
            </div>
        </div>
    );
}
