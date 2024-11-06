import { useEffect } from "react";
import { useNavigate } from "react-router-dom";

import { Grid, Paper, useTheme } from '@mui/material';

import { useAppDispatch, useAppSelector } from "../../../../common/redux/hooks";
import { authActions, loginAction } from "../../redux/authSlice";
import { LoginForm, LoginFormValues } from "./components/LoginForm/LoginForm";
import { Provider } from "react-redux";

export function LoginPage() {
    const dispatch = useAppDispatch();
    const navigate = useNavigate();
    const theme = useTheme();

    const {
        requestsMeta: { postLoginStatus },
    } = useAppSelector(state => state.auth);
    const isLoading = postLoginStatus === 'loading';

    useEffect(() => {
        if (postLoginStatus === 'success') {
            navigate('/');
        }
    }, [postLoginStatus]);

    useEffect(() => {
        return () => {
            dispatch(authActions.resetRequestsMeta());
        };
    }, []);

    const onSubmit = (values: LoginFormValues) => {
        dispatch(loginAction(values));
    };

    return (
        <Grid container>
            <Grid
             item
             lg={8}
             md={6}
             sm={4}
             sx={{
                backgroundRepeat: 'no-repeat',
                backgroundColor: theme.palette.background.default,
                backgroundSize: 'cover',
                backgroundPosition: 'center',
             }}
             xs={false}
            />
            <Grid component={Paper} elevation={6} item lg={4} md={6} sm={8} square xs={12}>
                <LoginForm isLoading={isLoading} onSubmit={onSubmit} />
            </Grid>
        </Grid>
    );
}
