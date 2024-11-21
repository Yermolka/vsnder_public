import { Divider, Grid2, Paper, Typography } from "@mui/material";
import { GetUserDto } from "../dto/user";
import { ProfilePicture } from "./ProfilePicture";

export function FullUserFrame(data: GetUserDto) {
    const notAvailable = "Не указано"

    return (
        // <Paper elevation={3} style={{ padding: "25px", margin: "10px" }}>
            <Grid2 container alignItems="stretch" justifyContent="center" spacing={2} columns={{ md: 6, xs: 3 }}>
                <Grid2 size={3} justifyItems="center" justifyContent="center" alignContent="center" alignItems="center">
                    <Typography>{data.orientation}, {data.year_of_study} курс</Typography>
                </Grid2>
                <Grid2 size={3} justifyItems="center" justifyContent="center" alignContent="center" alignItems="center">
                    <ProfilePicture userId={data.id} hasAvatar={data.has_avatar} />
                </Grid2>
                <Grid2 size={3} justifyItems="center" justifyContent="center" alignContent="center" alignItems="center">
                    <Typography>Возраст: {data.age || notAvailable}</Typography>
                </Grid2>
                <Grid2 size={3} justifyItems="center" justifyContent="center" alignContent="center" alignItems="center">
                    <Typography>Интересы: {data.interests || notAvailable}</Typography>
                    <Divider />
                    <Typography>Интересы на ВСН: {data.vsn_interests || notAvailable}</Typography>
                </Grid2>
                <Grid2 size={3} justifyItems="center" justifyContent="center" alignContent="center" alignItems="center">
                    <Typography>Любимые места поботать: {data.study_places || notAvailable}</Typography>
                    <Divider />
                    <Typography>Места, где хотелось бы побывать: {data.places_to_visit || notAvailable}</Typography>
                </Grid2>
                <Grid2 size={3} justifyItems="center" justifyContent="center" alignContent="center" alignItems="center">
                    <Typography>Любимая музыка: {data.music || notAvailable}</Typography>
                    <Divider />
                    <Typography>Любимые фильмы: {data.favorite_movies || notAvailable}</Typography>
                </Grid2>
                <Grid2 size={3} justifyItems="center" justifyContent="center" alignContent="center" alignItems="center">
                    <Typography>Религия: {data.religion || notAvailable}</Typography>
                    <Divider />
                    <Typography>Планы на будущее: {data.future_plans || notAvailable}</Typography>
                </Grid2>
                <Grid2 size={3} justifyItems="center" justifyContent="center" alignContent="center" alignItems="center">
                    <Typography>Взгляды на семью: {data.family_opinion || notAvailable}</Typography>
                    <Divider />
                    <Typography>Любимый ЯП: {data.favorite_programming_language || notAvailable}</Typography>
                </Grid2>
                <Grid2 size={3} justifyItems="center" justifyContent="center" alignContent="center" alignItems="center">
                    <Typography>Отношение к курению: {data.smoking || notAvailable}</Typography>
                    <Divider />
                    <Typography>Отношение к алкоголю: {data.drinking || notAvailable}</Typography>
                </Grid2>
                <Grid2 size={3} justifyItems="center" justifyContent="center" alignContent="center" alignItems="center">
                    <Typography>3 кумира: {data.top_3_people || notAvailable}</Typography>
                    <Divider />
                    <Typography>Статус?: {data.status || notAvailable}</Typography>
                </Grid2>
            </Grid2>
        // </Paper>
    )
}
