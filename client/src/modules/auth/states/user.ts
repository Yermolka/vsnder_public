import { SerializedError } from '@reduxjs/toolkit';

import { RequestStatus } from '../../../common/states/common';

export interface UserState {
  jwtToken: string | null;
}

export interface AuthState extends UserState {
  requestsMeta: {
    postLoginStatus: RequestStatus;
    postLoginError: SerializedError | null;
    postLogoutStatus: RequestStatus;
    postLogoutError: SerializedError | null;
    postUserRequestStatus: RequestStatus;
    postUserError: SerializedError | null;
  };
}
