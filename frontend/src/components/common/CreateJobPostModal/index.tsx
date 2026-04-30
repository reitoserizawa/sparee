import React, { useState } from 'react';
import { useParams } from 'react-router-dom';
import { useGetJobCategoriesQuery } from '../../../store/features/jobCategory/jobCategoryApi';
import requiredValidator from '../../ui/Form/validators/required';
import { useCreateJobPostMutation } from '../../../store/features/jobPost/jobPostApi';
import { isErrorWithMessage } from '../../../store/features/base/helpers';
import type { CreateJobPostModalProps } from './types';
import type { JobPostCreateState } from '../../../store/features/jobPost/types';
import Modal from '../../ui/Modal';
import Form from '../../ui/Form';
import FormInput from '../../ui/Form/FormInput';
import FormSelect from '../../ui/Form/FormSelect';
import FormTextarea from '../../ui/Form/FormTextarea';
import Button from '../../ui/Button';
import Error from '../../ui/Error';

const inputClass =
    'w-full border border-gray-200 rounded-lg px-3 py-2 text-sm text-gray-800 placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-indigo-400 focus:border-transparent transition';

const CreateJobPostModal: React.FC<CreateJobPostModalProps> = ({ onClose }) => {
    const { companyId } = useParams();
    const [showAddress, setShowAddress] = useState(false);
    const [createJobPost, { isLoading: isCreating, isError, error }] = useCreateJobPostMutation();
    const { data: categories, isLoading: categoriesLoading } = useGetJobCategoriesQuery(null);

    const initialValues: JobPostCreateState = {
        company_id: Number(companyId),
        job_category_id: undefined,
        title: '',
        description: '',
        salary: 0,
        address: undefined,
    };

    const handleSubmit = async (data: JobPostCreateState) => {
        try {
            const payload: JobPostCreateState = {
                ...data,
                address:
                    showAddress && data.address
                        ? {
                              country: 'USA',
                              street: data.address.street ?? '',
                              city: data.address.city ?? '',
                              state: data.address.state ?? '',
                              postal_code: data.address.postal_code ?? '',
                          }
                        : undefined,
            };
            await createJobPost(payload).unwrap();
            onClose();
        } catch (error) {
            console.error('Failed to create job post:', error);
        }
    };

    const categoryOptions = (categories ?? []).map(cat => ({ value: cat.id, label: cat.name }));

    return (
        <Modal open title='New Job Post' onClose={onClose}>
            <Form<JobPostCreateState> initialValues={initialValues} onSubmit={handleSubmit} className='space-y-4'>
                <FormInput<JobPostCreateState>
                    name='title'
                    label='Job Title*'
                    type='text'
                    validators={[requiredValidator()]}
                    className={inputClass}
                />

                <FormSelect<JobPostCreateState>
                    name='job_category_id'
                    label='Category*'
                    validators={[requiredValidator()]}
                    options={categoryOptions}
                    placeholder={categoriesLoading ? 'Loading...' : 'Select category'}
                    disabled={categoriesLoading}
                    className={`${inputClass} bg-white disabled:text-gray-400`}
                />

                <FormInput<JobPostCreateState>
                    name='salary'
                    label='Salary*'
                    type='number'
                    validators={[requiredValidator()]}
                    className={inputClass}
                />

                <FormTextarea<JobPostCreateState>
                    name='description'
                    label='Description*'
                    validators={[requiredValidator()]}
                    placeholder='Describe the role, responsibilities, and requirements...'
                    rows={4}
                    className={`${inputClass} resize-none`}
                />

                <div>
                    <button
                        type='button'
                        onClick={() => setShowAddress(v => !v)}
                        className='flex items-center gap-2 text-xs font-medium text-indigo-600 hover:text-indigo-800 transition'
                    >
                        <span className='text-base leading-none'>{showAddress ? '−' : '+'}</span>
                        {showAddress ? 'Remove address' : 'Add address (optional)'}
                    </button>
                </div>

                {showAddress && (
                    <>
                        <FormInput<JobPostCreateState>
                            name='address.street'
                            label='Street*'
                            type='text'
                            validators={[requiredValidator()]}
                            className={inputClass}
                        />
                        <FormInput<JobPostCreateState>
                            name='address.city'
                            label='City*'
                            type='text'
                            validators={[requiredValidator()]}
                            className={inputClass}
                        />
                        <FormInput<JobPostCreateState>
                            name='address.state'
                            label='State*'
                            type='text'
                            validators={[requiredValidator()]}
                            className={inputClass}
                        />
                        <FormInput<JobPostCreateState>
                            name='address.postal_code'
                            label='Postal Code*'
                            type='text'
                            validators={[requiredValidator()]}
                            className={inputClass}
                        />
                    </>
                )}
                {isError && isErrorWithMessage(error) && <Error message={error?.data?.message} />}
                <div className='flex justify-end gap-2 pt-4 border-t border-gray-100'>
                    <Button variant='ghost' className='px-4 py-2 rounded-full text-sm' onClick={onClose}>
                        Cancel
                    </Button>

                    <Button
                        variant='primary'
                        className='px-4 py-2 rounded-full text-sm'
                        type='submit'
                        disabled={isCreating}
                    >
                        {isCreating ? 'Creating...' : 'Create Job Post'}
                    </Button>
                </div>
            </Form>
        </Modal>
    );
};

export default CreateJobPostModal;
