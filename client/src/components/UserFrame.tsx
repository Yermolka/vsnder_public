import { Button, Grid2, Paper, useTheme } from "@mui/material";
import { GetShortUserDto } from "../dto/user";
import { ProfilePicture } from "./ProfilePicture";

export function UserFrame(data: GetShortUserDto) {
    return (
        <Paper elevation={3} style={{ padding: "10px", justifyContent: "center" }} sx={{ width: { xs: "40%", md: "30%", lg: "20%" } }} key={data.id}>
            <Grid2 container size={12} direction="row" spacing={2} justifyContent="center" style={{ height: '100%', width: '100%' }} alignItems="stretch">
                <Grid2 size={6} justifyItems="center" justifyContent="flex-end">
                    <ProfilePicture userId={data.id} hasAvatar={data.has_avatar} />
                    {data.orientation ? <p>Программа: {data.orientation}</p> : null}
                    <p>Курс: {data.year_of_study}</p>
                </Grid2>
                <Grid2 size={6} justifyItems="center" justifyContent="flex-start">
                    <Button fullWidth sx={{ height: "90%" }} variant="contained" href={`/users/${data.id}`}>{data.first_name} {data.last_name}</Button>
                </Grid2>
            </Grid2>
        </Paper>
    )
}
