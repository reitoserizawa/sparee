class DateUtils {
    static formatDate(date: Date): string {
        const y = date.getFullYear();
        const m = String(date.getMonth() + 1).padStart(2, '0');
        const d = String(date.getDate()).padStart(2, '0');
        return `${y}-${m}-${d}`;
    }

    static parseDate = (date: string) => {
        const [y, m, d] = date.split('-').map(Number);
        return new Date(y, m - 1, d);
    };
}

export default DateUtils;
