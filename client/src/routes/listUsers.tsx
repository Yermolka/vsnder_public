import { Box, Grid2 } from "@mui/material";
import { useLoaderData } from "react-router-dom";
import { UserFrame } from "../components/UserFrame";
import { GetUserDto } from "../dto/user";
import { getUsers } from "../api/user";

export function ListUsers() {
    const users = useLoaderData() as Array<GetUserDto> | undefined;
    console.log(users);

    return (
        <Box className="list-users">
            <Grid2 container spacing={2}>
                { users ? users.map((user) => UserFrame(user)) : null}
            </Grid2>
        </Box>
    )
}


export async function listUsersLoader() {
    return await getUsers();

    // return [
    //     {
    //         id: 1,
    //         firstName: "Andrey",
    //         lastName: "Yermoshin",
    //         age: 24,
    //     },
    //     {
    //         id: 2,
    //         firstName: "Max",
    //         lastName: "Hass",
    //     }
    // ]
}
