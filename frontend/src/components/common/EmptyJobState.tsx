const EmptyJobState = ({ message }: { message: string }) => {
    return (
        <div className='h-60 w-90 rounded-2xl shrink-0 bg-gradient-to-br from-blue-500 to-cyan-500 p-6 text-white flex items-center justify-center text-center'>
            <div>
                <h3 className='text-xl font-semibold mb-2'>No Jobs Found</h3>
                <p className='text-sm opacity-90'>{message}</p>
            </div>
        </div>
    );
};

export default EmptyJobState;
