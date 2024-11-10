import { Box, Grid2 } from "@mui/material";
import { redirect, useLoaderData } from "react-router-dom";
import { UserFrame } from "../components/UserFrame";
import { GetUserDto } from "../dto/user";
import { getUsers } from "../api/user";

export function ListUsers() {
    const users = useLoaderData() as Array<GetUserDto> | undefined;

    return (
        <Box className="list-users">
            <Grid2 container spacing={2} columns={6} justifyContent="center">
                { users ? users.map((user) => UserFrame(user)) : null}
            </Grid2>
        </Box>
    )
}


export async function listUsersLoader() {
    const res = await getUsers();
    if (res.status === 200) {
        return res.data;
    } else if (res.status === 401) {
        return redirect("/logout");
    }

    return null;
}
