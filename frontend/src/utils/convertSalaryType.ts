const convertSalaryType = (salaryType: string) => {
    switch (salaryType) {
        case 'hourly':
            return 'hour';
        case 'daily':
            return 'day';
        case 'monthly':
            return 'month';
        default:
            return 'N/A';
    }
};

export default convertSalaryType;
