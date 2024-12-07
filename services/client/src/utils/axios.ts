import axios, { AxiosError, isCancel } from 'axios';
import axiosRetry from 'axios-retry';

const ax = axios.create({
    baseURL: '/api',
});

ax.interceptors.response.use(response => {
    return response;
});

axiosRetry(ax, {
    retryDelay: axiosRetry.exponentialDelay,
    retryCondition: error => {
        if (isCancel(error)) {
            return false;
        }

        const axiosError = error as AxiosError;

        if (axiosError.status && (axiosError.status === 404 || axiosError.status === 401)) {
            return false;
        }

        if (!axiosError.response) {
            return true;
        }

        return axiosRetry.isNetworkOrIdempotentRequestError(error);
    },
});

export { ax };

export function axiosErrorGuard(err: any): err is AxiosError {
    return err.isAxiosError != null;
}
