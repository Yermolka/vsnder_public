import { createAsyncThunk, createSlice } from '@reduxjs/toolkit';

import { serializeError } from '../../app/utils/error/serializeError';

import { logout, login as postLogin } from '../api/auth';
import { AuthState, UserState } from '../states/user';
import { userInfoStorage } from '../utils/localStorage';

const sliceName = 'authSlice';
const userInfo = userInfoStorage.load();
let jwtToken: UserState['jwtToken'] = null;

if (userInfo !== null) {
    jwtToken = userInfo.jwtToken;
}

export const initialState: AuthState = {
    jwtToken,
    requestsMeta: {
        postLoginStatus: 'idle',
        postLoginError: null,
        postLogoutStatus: 'idle',
        postLogoutError: null,
        postUserRequestStatus: 'idle',
        postUserError: null,
    },
};

export const loginAction = createAsyncThunk(
    `${sliceName}/login`,
    async ({ username, password }: {username: string; password: string;}) => {
        try {
            await postLogin({ username, password });
            const info = {
                jwtToken: null,
            };
            return info;
        } catch (err) {
            throw serializeError(err);
        }
    },
);

export const logoutAction = createAsyncThunk(`${sliceName}/logout`, async () => {
    try {
        return await logout();
    } catch (err) {
        throw serializeError(err);
    }
});

const slice = createSlice({
    name: sliceName,
    initialState,
    reducers: {
        resetRequestsMeta: state => {
            state.requestsMeta = { ...initialState.requestsMeta };
        },
    },
    extraReducers(builder) {
        builder
            .addCase(loginAction.pending, (state, _) => {
                state.requestsMeta.postLoginStatus = 'loading';
                state.requestsMeta.postLoginError = null;
                userInfoStorage.clear();
            })
            .addCase(loginAction.fulfilled, (state, action) => {
                state.jwtToken = action.payload.jwtToken;
                state.requestsMeta.postLoginStatus = 'success';
                state.requestsMeta.postLoginError = null;
                userInfoStorage.save(action.payload);
            })
            .addCase(loginAction.rejected, (state, action) => {
                state.requestsMeta.postLoginStatus = 'failed';
                state.requestsMeta.postLoginError = action.error;
                userInfoStorage.clear();
            });

        builder
            .addCase(logoutAction.pending, (state, _) => {
                state.requestsMeta.postLogoutStatus = 'loading';
                state.requestsMeta.postLogoutError = null;
                userInfoStorage.clear();
            })
            .addCase(logoutAction.fulfilled, (state, _) => {
                state.jwtToken = null;

                state.requestsMeta.postLogoutStatus = 'success';
                state.requestsMeta.postLogoutError = null;
                userInfoStorage.clear();
            })
            .addCase(logoutAction.rejected, (state, action) => {
                state.jwtToken = null;

                state.requestsMeta.postLogoutStatus = 'failed';
                state.requestsMeta.postLogoutError = action.error;
                userInfoStorage.clear();
            });
    },
});

export const authActions = slice.actions;
export const authReducer = slice.reducer;
