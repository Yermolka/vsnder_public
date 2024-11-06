import { useEffect } from "react";
import { useNavigate } from "react-router-dom";

import { Grid, Paper, useTheme } from '@mui/material';

import { useAppDispatch, useAppSelector } from "../../../../common/redux/hooks";
import { authActions, loginAction } from "../../redux/authSlice";
import { LoginForm, LoginFormValues } from "./components/LoginForm/LoginForm";
import { PRIMARY_COLOR, SECONDARY_COLOR, THIRD_COLOR } from "../../../../common/consts/common";

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
        <Grid 
          container 
          spacing={0} 
          direction='column' 
          justifyContent='center' 
          component={Paper} 
          elevation={6} 
          sx={{
            minHeight: '100vh',
            backgroundColor: THIRD_COLOR,
            backgroundSize: 'cover',
            backgroundPosition: 'center',
          }}>
            <LoginForm isLoading={isLoading} onSubmit={onSubmit} />
        </Grid>
    );
}
