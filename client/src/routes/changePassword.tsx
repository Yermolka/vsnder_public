import { ErrorMessage, Form, Formik } from "formik";
import { changePasswordValidationSchema } from "../utils/validation";
import { Button, Grid2, TextField } from "@mui/material";
import { postUserChangePassword } from "../api/user";
import './extra.scss';

export function ChangePassword() {
    return (
        <Formik 
          initialValues={{old_password: '', new_password: '', new_password_re: ''}}
          validationSchema={changePasswordValidationSchema}
          onSubmit={(values, { setSubmitting }) => {
            changePasswordAction(values).catch(console.error);
            setSubmitting(false);
          }}>
            {props => 
                <Form className="change-password-form">
                    <Grid2 container spacing={2} columns={3}>
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
                        <Grid2 size={1} offset={1} alignContent="center">
                            <Button variant="contained" type="submit" disabled={props.isSubmitting}>Изменить</Button>
                        </Grid2>
                    </Grid2>
                </Form>
            }
          </Formik>
    )
}


export async function changePasswordAction(params: any) {
    return await postUserChangePassword({old_password: params.old_password, new_password: params.new_password});
}
