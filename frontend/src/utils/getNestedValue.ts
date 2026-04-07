const getNestedValue = (obj: unknown, path: string): unknown =>
    path.split('.').reduce((acc, key) => (acc as Record<string, unknown>)?.[key], obj);

export default getNestedValue;
