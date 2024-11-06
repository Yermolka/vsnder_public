import LockOutlinedIcon from '@mui/icons-material/LockOutlined';
import { Avatar, Box, Button, Divider, Grid, Link, MenuItem, TextField, Typography } from '@mui/material';
import { Form, Formik } from 'formik';
import * as yup from 'yup';

import { CircularProgress } from '../../../../../../common/components/CircularProgress/CircularProgress';
import { PasswordField } from '../../../../../../common/components/PasswordField/PasswordField';
import { useColors } from '../../../../../../common/hooks/useColors';

import './LoginForm.scss';
import { FOURTH_COLOR } from '../../../../../../common/consts/common';

export interface LoginFormValues {
    username: string;
    password: string;
}

interface LoginFormProps {
    isLoading: boolean;
    onSubmit: (values: LoginFormValues) => void;
}

const validationSchema = yup.object({
    username: yup.string().required('Обязательное поле Логин'),
    password: yup.string().required('Обязательное поле Пароль'),
});

export function LoginForm({ isLoading, onSubmit }: LoginFormProps) {
    const { primaryIconColor, primaryIconTextColor } = useColors();

    return (
        <Box className="login-form">
            <Avatar sx={{bgcolor: primaryIconColor, color: primaryIconTextColor, m: 1, marginBlockEnd: '24px' }}>
                <LockOutlinedIcon />
            </Avatar>
            <Typography component="h1" variant="h5">
                Войти
            </Typography>

            <Formik
              initialValues={{
                username: '',
                password: '',
              }}
              onSubmit={onSubmit}
              validationSchema={validationSchema}
            >
                {formik => (
                    <Form className="login-form-content">
                        <Grid container spacing={2}>
                            <Grid item xs={12}>
                                <TextField
                                  autoComplete='username'
                                  autoFocus
                                  data-cy='login-form-username'
                                  disabled={isLoading}
                                  error={formik.touched.username && Boolean(formik.errors.username)}
                                  fullWidth
                                  helperText={formik.touched.username && formik.errors.username}
                                  id='login-form-username'
                                  label='Username'
                                  name='username'
                                  onChange={formik.handleChange}
                                  value={formik.values.username}
                                />
                            </Grid>
                            <Grid item xs={12}>
                                <PasswordField
                                  autoComplete='current-password'
                                  data-cy='login-form-password'
                                  disabled={isLoading}
                                  error={formik.touched.password && Boolean(formik.errors.password)}
                                  fullWidth
                                  helperText={formik.touched.password && formik.errors.password}
                                  id='login-form-password'
                                  label='Password'
                                  name='password'
                                  onChange={formik.handleChange}
                                  value={formik.values.password}
                                />
                            </Grid>
                            <Grid item xs={12}>
                                <Box className='login-form-submit'>
                                    <Button
                                      color='secondary'
                                      data-cy='login-form-submit'
                                      disabled={isLoading}
                                      fullWidth
                                      id='login-form-submit'
                                      type='submit'
                                      variant='contained'
                                    >
                                        {isLoading ? <CircularProgress size={25} /> : "Войти"}
                                    </Button>
                                </Box>
                            </Grid>
                        </Grid>
                    </Form>
                )}
            </Formik>
        </Box>
    )
}
