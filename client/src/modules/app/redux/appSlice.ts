import { PayloadAction, createSlice } from "@reduxjs/toolkit";

import { AppState, SnackBarMsg } from "../states/app";

const sliceName = 'appSlice';

export const initialState: AppState = {
    snackbarMsgQueue: [],
    appLockMsg: null,
    isAppLocked: false,
}

const slice = createSlice({
    name: sliceName,
    initialState,
    reducers: {
        pushSnackbarMsg(state, action: PayloadAction<SnackBarMsg>) {
            state.snackbarMsgQueue.push(action.payload);
        },
        popSnackbarMsg(state) {
            state.snackbarMsgQueue.shift();
        },
        lockApp(state, action: PayloadAction<string>) {
            state.isAppLocked = true;
            state.appLockMsg = action.payload;
        },
        unlockApp(state) {
            state.isAppLocked = false;
            state.appLockMsg = null;
        },
    },
});

export const appActions = slice.actions;
export const appReducer = slice.reducer;
