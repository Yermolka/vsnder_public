import { Button, Grid2, Paper, useTheme } from "@mui/material";
import { GetUserDto } from "../dto/user";
import { ProfilePicture } from "./ProfilePicture";

export function UserFrame(data: GetUserDto) {
    return (
        <Paper elevation={3} style={{ padding: "10px" }} key={data.id}>
            <Grid2 container spacing={2} justifyContent="center" alignItems="center">
                <Grid2 size={12} justifyContent="center" alignItems="center">
                    <ProfilePicture userId={data.id} />
                </Grid2>
                 <Grid2 size={12} justifyContent="center" alignItems="center">
                    <Button variant="contained" href={`/users/${data.id}`}><h1>{data.first_name} {data.last_name}</h1></Button>
                    {data.age ? <p>Age: {data.age}</p> : null}
                 </Grid2>
            </Grid2>
        </Paper>
    )
}
