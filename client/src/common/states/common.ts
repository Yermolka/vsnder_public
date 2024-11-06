import { SerializedError } from "@reduxjs/toolkit";

import { User } from "../models/user";

export type RequestStatus = 'idle' | 'loading' | 'success' | 'failed';

export interface RequestsMeta {
    requestsMeta: Record<string, any>;
}

export interface CommonState {
    firstLoadInitialized: boolean;
    userInfo: User | null;
    requestsMeta: {
        userInfoStatus: RequestStatus;
        userInfoError: SerializedError | null;
    };
}
