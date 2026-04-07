const passwordMatchValidator = <State extends { password: string; confirm_password: string }>() => {
    return (data: Partial<State>) => {
        if (data.password !== data.confirm_password) {
            return ['Passwords must match'];
        }
        return [];
    };
};

export default passwordMatchValidator;
