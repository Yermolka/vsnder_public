import { Card, CardActionArea, CardContent, Grid2, Paper, Typography } from "@mui/material";
import { GetShortUserDto } from "../dto/user";
import { ProfilePicture } from "./ProfilePicture";

export function UserFrame(data: GetShortUserDto) {
    return (
        <Card elevation={0} sx={{ width: { xs: "40%", md: "30%", lg: "20%" }, minWidth: { xs: "40%", md: "30%", lg: "20%" }, borderRadius: {xs: 5, md: 10, lg: 15}, padding: "10px", justifyContent: "center" }} key={data.id}>
            <CardActionArea>
                <CardContent onClick={() => window.location.assign(`/users/${data.id}`)}>
                    <Grid2 container columns={3} spacing={2} textAlign="center" justifyContent="center" style={{ height: '100%', width: '100%' }} alignItems="center" justifyItems="center" alignContent="center">
                        <Grid2 size={3}>
                            <ProfilePicture fileId={data.file_id} />
                        </Grid2>
                        <Grid2 size={3}>
                            <Typography textAlign="center" fontSize={{ lg: 24, md: 24, xs: 10 }} noWrap>{data.last_name} {data.first_name}</Typography>
                        </Grid2>
                        <Grid2 size={3} textAlign="center">
                            {<p>{data.orientation ? data.orientation : null}</p>}
                            <p>{data.year_of_study} курс</p>
                        </Grid2>
                    </Grid2>
                </CardContent>
            </CardActionArea>
        </Card>
    )
}
