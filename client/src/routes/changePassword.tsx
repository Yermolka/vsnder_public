import { ErrorMessage, Form, Formik } from "formik";
import { changePasswordValidationSchema } from "../utils/validation";
import { Button, Grid2, Paper, TextField, Typography } from "@mui/material";
import { postUserChangePassword } from "../api/user";
import './extra.scss';
import { useState } from "react";

export function ChangePassword() {
    const [postMsg, setPostMsg] = useState<string | null>(null);
    
    return (
        <Paper elevation={6}>
            <Formik 
            initialValues={{old_password: '', new_password: '', new_password_re: ''}}
            validationSchema={changePasswordValidationSchema}
            onSubmit={(values, { setSubmitting }) => {
                changePasswordAction(values).then((value: string | null) => {
                    if (!value) {
                        setPostMsg('Пароль успешно изменен');
                    } else {
                        setPostMsg(value)
                    }
                });
                setSubmitting(false);
            }}>
                {props => 
                    <Form className="change-password-form">
                        <Grid2 container spacing={2} columns={3} justifyContent="center">
                            <Grid2 size={3}>
                                <TextField 
                                type="password" 
                                name="old_password" 
                                label='Старый пароль' 
                                value={props.values.old_password} 
                                onChange={props.handleChange}
                                helperText={props.errors.old_password}
                                error={Boolean(props.errors.old_password)}
                                fullWidth/>
                            </Grid2>
                            <Grid2 size={3}>
                                <TextField 
                                type="password" 
                                name="new_password" 
                                label='Новый пароль' 
                                value={props.values.new_password} 
                                onChange={props.handleChange}
                                helperText={props.errors.new_password}
                                error={Boolean(props.errors.new_password)}
                                fullWidth/>
                            </Grid2>
                            <Grid2 size={3}>
                                <TextField 
                                type="password" 
                                name="new_password_re" 
                                label='Подтверждение пароля' 
                                value={props.values.new_password_re} 
                                onChange={props.handleChange}
                                helperText={props.errors.new_password_re}
                                error={Boolean(props.errors.new_password_re)}
                                fullWidth/>
                            </Grid2>
                            <Grid2 size={3} alignContent="center" justifyContent="center" sx={{ width: '100%'}}>
                                <Button fullWidth variant="contained" type="submit" disabled={props.isSubmitting}>Изменить</Button>
                                {postMsg ? <Typography variant="inherit" color="error">{ postMsg }</Typography> : null }
                            </Grid2>
                        </Grid2>
                    </Form>
                }
            </Formik>
          </Paper>
    )
}


export async function changePasswordAction(params: any): Promise<string | null> {
    return await postUserChangePassword({old_password: params.old_password, new_password: params.new_password});
}
