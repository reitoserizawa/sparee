import React from 'react';
import { useNavigate } from 'react-router-dom';

import requiredValidator from '../ui/Form/validators/required';
import { isErrorWithMessage } from '../../store/features/base/helpers';

import type { CompanyCreateState } from '../../store/features/company/type';

import Form from '../ui/Form';
import FormInput from '../ui/Form/FormInput';
import Error from '../ui/Error';
import Button from '../ui/Button';
import { useCreateCompanyMutation } from '../../store/features/company/companyApi';

const CompanyRegisterPage = (): React.ReactElement => {
    const initialValues: CompanyCreateState = {
        name: '',
        address: {
            street: '',
            city: '',
            state: '',
            postal_code: '',
            country: 'USA',
        },
    };
    const navigate = useNavigate();
    const [createCompany, { isLoading, isError, error }] = useCreateCompanyMutation();

    const handleSubmit = async (data: CompanyCreateState) => {
        try {
            await createCompany(data).unwrap();
            navigate('/');
        } catch (err) {
            console.error('Failed to create company:', err);
        }
    };

    return (
        <div className='min-h-screen flex items-center justify-center bg-gray-50 px-4'>
            <div className='w-full max-w-md bg-white shadow-lg rounded-2xl p-8'>
                <div className='mb-6 text-center'>
                    <h1 className='text-2xl font-semibold tracking-tight'>Create a company</h1>
                    <p className='text-sm text-gray-500 mt-1'>
                        Fill in the details below to create your company profile
                    </p>
                </div>

                <Form<CompanyCreateState> initialValues={initialValues} onSubmit={handleSubmit} className='space-y-4'>
                    <FormInput<CompanyCreateState>
                        name='name'
                        label='Name*'
                        type='text'
                        validators={[requiredValidator()]}
                    />
                    <FormInput<CompanyCreateState>
                        name='address.street'
                        label='Street*'
                        type='text'
                        validators={[requiredValidator()]}
                    />
                    <FormInput<CompanyCreateState>
                        name='address.city'
                        label='City*'
                        type='text'
                        validators={[requiredValidator()]}
                    />
                    <FormInput<CompanyCreateState>
                        name='address.state'
                        label='State*'
                        type='text'
                        validators={[requiredValidator()]}
                    />
                    <FormInput<CompanyCreateState>
                        name='address.postal_code'
                        label='Postal Code*'
                        type='text'
                        validators={[requiredValidator()]}
                    />
                    {isError && isErrorWithMessage(error) && <Error message={error?.data?.message} />}
                    <Button type='submit' disabled={isLoading} className='w-full rounded-lg py-2 text-sm'>
                        {isLoading ? 'Creating company...' : 'Create'}
                    </Button>
                </Form>

                <p className='text-sm text-center text-gray-500 mt-6'>
                    <button onClick={() => navigate(-1)} className='text-black font-medium hover:underline'>
                        Go back
                    </button>
                </p>
            </div>
        </div>
    );
};

export default CompanyRegisterPage;
