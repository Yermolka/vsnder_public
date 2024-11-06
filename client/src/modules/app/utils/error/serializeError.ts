import { SerializedError } from "@reduxjs/toolkit";
import isEmpty from 'lodash/isEmpty'

import { axiosErrorGuard } from "../../../../common/axios";

export enum SerializedErrors {
    NO_RESPONSE = 'no response',
};

export function serializeError(err: any): SerializedError {
    const serializedError: SerializedError = {
        name: err?.name,
        message: err?.message,
        stack: err?.stack,
        code: err?.code,
    };

    if (axiosErrorGuard(err)) {
        if (err.response) {
            serializedError.name = err.response.statusText;
            serializedError.code = err.response?.status.toString();
            serializedError.message = '';

            if (err.response.data != null && typeof err.response.data === 'string') {
                serializedError.message = err.response.data;
            }

            const params = isEmpty(err.response.config.params) ? 'empty' : JSON.stringify(err.response.config.params);

            serializedError.message = `${serializedError.message}. Params: ${params}`;
        } else if (err.request) {
            serializedError.name = SerializedErrors.NO_RESPONSE;
            serializedError.message = 'Got no response';
        }
    }

    return serializedError;
}
