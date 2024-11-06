export type MsgSeverity = 'error' | 'warning' | 'info' | 'success';

export interface SnackBarMsg {
    msg: string;
    severity: MsgSeverity;
}

export interface AppState {
    snackbarMsgQueue: SnackBarMsg[];
    isAppLocked: boolean;
    appLockMsg: string | null;
}
