import { Button, Grid2, TextField } from "@mui/material";
import { useEffect } from "react";
import { Form, redirect, useNavigate } from "react-router-dom";
import { UserAuthDto } from "../dto/user";
import { postLogin } from "../api/auth";

export function LoginPage() {
    return (
        <Form method='post'>
            <Grid2 container spacing={2} size={12}>
                <Grid2 size={12}>
                    <h1>Войти</h1>
                </Grid2>
                <Grid2 size={12}>
                    <TextField id='username' label='Логин' />
                </Grid2>
                <Grid2 size={12}>
                    <TextField id='password' type='password' label='Пароль' />
                </Grid2>
                <Grid2 size={12}>
                    <Button type='submit' color="primary">Войти</Button>
                </Grid2>
            </Grid2>
        </Form>
    )
}


export async function loginPageAction(params: any) {
    const res = await postLogin(params);
    if (res.status === 200) {
        localStorage.setItem("userId", JSON.stringify(res.data.userId));
        return redirect("/users");
    }

    return null;
}
