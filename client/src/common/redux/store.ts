import { Action, AnyAction, CombinedState, ThunkAction, combineReducers, configureStore } from '@reduxjs/toolkit';

import { appReducer, initialState as appInitialState } from '../../modules/app/redux/appSlice';
import { authReducer, initialState as authInitialState } from '../../modules/auth/redux/authSlice';
import { commonReducer, initialState as commonInitialState } from "./commonSlice";

import { RESET_STORE_TYPE } from './actions';


const combinedReducer = combineReducers({
    app: appReducer,
    auth: authReducer,
    common: commonReducer,
});

const rootReducer = (state: CombinedState<ReturnType<typeof combinedReducer>> | undefined, action: AnyAction) => {
    if (action.type === RESET_STORE_TYPE) {
        return initialState;
    }
    return combinedReducer(state, action);
}

const initialState = {
    app: appInitialState,
    auth: authInitialState,
    common: commonInitialState,
};

export const store = configureStore({
    reducer: rootReducer,
    devTools: true,
});

export type RootState = ReturnType<typeof store.getState>;
export type AppDispatch = typeof store.dispatch;
export type AppThunk<ReturnType = void> = ThunkAction<ReturnType, RootState, unknown, Action<string>>;
