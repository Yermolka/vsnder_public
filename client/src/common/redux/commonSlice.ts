import { createAsyncThunk, createSlice, PayloadAction } from '@reduxjs/toolkit';

import { getUser } from "../api/user";
import { CommonState } from "../states/common";

import { serializeError } from "../../modules/app/utils/error/serializeError";

const sliceName = 'common-reducer';

export const initialState: CommonState = {
    firstLoadInitialized: false,
    userInfo: null,
    requestsMeta: {
        userInfoStatus: 'idle',
        userInfoError: null,
    },
};

export const getUserAction = createAsyncThunk(`${sliceName}/getUser`, async () => {
    try {
        return await getUser();
    } catch (err) {
        throw serializeError(err);
    }
});

const slice = createSlice({
    name: sliceName,
    initialState,
    reducers: {
        setFirstLoadInitialized(state, action: PayloadAction<boolean>) {
            state.firstLoadInitialized = action.payload;
        },
        resetRequestsMeta(state) {
            state.requestsMeta = initialState.requestsMeta;
        },
    },
    extraReducers: builder => {
        builder
            .addCase(getUserAction.pending, state => {
                state.requestsMeta.userInfoStatus = 'loading';
            })
            .addCase(getUserAction.fulfilled, (state, action) => {
                state.requestsMeta.userInfoStatus = 'success';
                state.userInfo = action.payload;
            })
            .addCase(getUserAction.rejected, (state, action) => {
                state.requestsMeta.userInfoStatus = 'failed';
                state.requestsMeta.userInfoError = action.error;
            });
    },
});

export const commonActions = slice.actions;
export const commonReducer = slice.reducer;
