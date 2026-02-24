export function isErrorWithMessage(error: unknown): error is { data: { message: string } } {
    if (typeof error !== 'object' || error === null) {
        return false;
    }

    if (!('data' in error)) {
        return false;
    }

    const data = (error as { data: unknown }).data;

    if (typeof data !== 'object' || data === null) {
        return false;
    }

    if (!('message' in data)) {
        return false;
    }

    return typeof (data as { message: unknown }).message === 'string';
}
