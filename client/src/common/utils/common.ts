export class VsnderLocalStorage<T extends object | string> {
    constructor(public storageKey: string) {}

    save (value: T) {
        localStorage.setItem(this.storageKey, JSON.stringify(value));
    }

    load(): T | null {
        const serialized = localStorage.getItem(this.storageKey);

        return serialized ? JSON.parse(serialized) : null;
    }

    clear() {
        localStorage.removeItem(this.storageKey);
    }
}
