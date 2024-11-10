import { Button, Grid2, Paper, useTheme } from "@mui/material";
import { GetUserDto } from "../dto/user";
import { ProfilePicture } from "./ProfilePicture";

export function UserFrame(data: GetUserDto) {
    return (
        <Paper elevation={3} style={{ padding: "10px", justifyContent: "center" }} sx={{ width: { xs: "40%", md: "30%", lg: "20%" } }} key={data.id}>
            <Grid2 container size={12} direction="row" spacing={2} justifyContent="center" style={{ height: '100%', width: '50%' }} alignItems="stretch">
                <Grid2 size={6} justifyContent="center">
                    <ProfilePicture userId={data.id} />
                    {data.age ? <p>Age: {data.age}</p> : null}
                    {/* Добавить курс, мб по дефолту по нему группировать */}
                </Grid2>
                <Grid2 size={6} justifyContent="center">
                    <Button variant="contained" href={`/users/${data.id}`}>{data.first_name} {data.last_name}</Button>
                </Grid2>
            </Grid2>
        </Paper>
    )
}
