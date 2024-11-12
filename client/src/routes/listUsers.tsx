import { Box, Grid2 } from "@mui/material";
import { redirect, useLoaderData } from "react-router-dom";
import { UserFrame } from "../components/UserFrame";
import { GetUserDto } from "../dto/user";
import { getUsers } from "../api/user";

export function ListUsers() {
    const users = useLoaderData() as Array<GetUserDto> | undefined;

    return (
        <Box className="list-users">
            <Grid2 container direction="row" spacing={2} columns={{md: 12, xs: 6}} alignItems="stretch" justifyContent="center">
                { users ? users.map((user) => UserFrame(user)) : null}
            </Grid2>
        </Box>
    )
}


export async function listUsersLoader() {
    const res = await getUsers();

    return res;
}
