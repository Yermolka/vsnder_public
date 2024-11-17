import { Divider, Grid2, Paper, Typography } from "@mui/material";
import { GetUserDto } from "../dto/user";
import { ProfilePicture } from "./ProfilePicture";

export function FullUserFrame(data: GetUserDto) {
    return (
        
        <Paper elevation={3} style={{ padding: "25px", margin: "10px" }}>
            <Grid2 container alignItems="stretch" justifyContent="center" spacing={2} columns={{ md: 6, xs: 3 }}>
                <Grid2 size={3}>
                    <ProfilePicture userId={data.id} hasAvatar={data.has_avatar} />
                </Grid2>
                <Grid2 size={3}>
                    <Typography>{data.first_name} {data.last_name}</Typography>
                    <Divider />
                    <Typography>{data.orientation}, {data.year_of_study} курс</Typography>
                </Grid2>
            </Grid2>
        </Paper>
    )
}
