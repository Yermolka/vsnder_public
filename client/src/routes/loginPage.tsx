import { Button, Grid2, TextField } from "@mui/material";
import { useEffect } from "react";
import { redirect, useNavigate } from "react-router-dom";
import { UserAuthDto } from "../dto/user";
import { postLogin } from "../api/auth";
import { Formik, Form } from "formik";

export function LoginPage() {
    const navigate = useNavigate();
    
    return (
        <Formik
         initialValues={{username: '', password: ''}}
         onSubmit={(values, { setSubmitting }) => {
            loginPageAction(values).catch(console.error).finally(() => navigate("/users"));
            setSubmitting(false);
         }}>
            {props => 
                <Form>
                    <Grid2 container spacing={2} size={12}>
                        <Grid2 size={12}>
                            <h1>Войти</h1>
                        </Grid2>
                        <Grid2 size={12}>
                            <TextField name='username' label='Логин' value={props.values.username} onChange={props.handleChange} />
                        </Grid2>
                        <Grid2 size={12}>
                            <TextField name='password' type='password' label='Пароль' value={props.values.password} onChange={props.handleChange}/>
                        </Grid2>
                        <Grid2 size={12}>
                            <Button type='submit' variant="contained" disabled={props.isSubmitting}>Войти</Button>
                        </Grid2>
                    </Grid2>
                </Form>
            }
        </Formik>
    )
}


export async function loginPageAction(data: UserAuthDto) {
    const res = await postLogin(data);
    if (res.status === 200) {
        localStorage.setItem("userId", JSON.stringify(res.data.userId));
    }

    return null;
}
