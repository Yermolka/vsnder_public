import { Divider, Grid2, Paper, Typography } from "@mui/material";
import { GetUserDto } from "../dto/user";
import { ProfilePicture } from "./ProfilePicture";
import { FullUserOneLine } from "./FullUserOneLine";

export function FullUserFrame(data: GetUserDto) {
    const notAvailable = "Не указано"

    return (
        <Grid2 container alignItems="center" alignContent="center" justifyItems="center" justifyContent="center" spacing={2} columns={6} width={{lg: "50%", md: "70%", xs: "90%"}}>
            <Grid2 size={6} justifyItems="center" justifyContent="center" alignContent="center" alignItems="center">
                <ProfilePicture userId={data.id} hasAvatar={data.has_avatar} />
            </Grid2>
            <Grid2 size={6} justifyItems="center" justifyContent="center" alignContent="center" alignItems="center">
                <Typography>{data.orientation ? data.orientation + "," : null} {data.year_of_study} курс</Typography>
            </Grid2>
            <FullUserOneLine name="Семейное положение" value={data.status} />
            <FullUserOneLine name="Возраст" value={data.age} />
            <FullUserOneLine name="Взгляды на семью" value={data.family_opinion} />
            <FullUserOneLine name="Отношение к курению" value={data.smoking} />
            <FullUserOneLine name="Отношение к алкоголю" value={data.drinking} />
            <FullUserOneLine name="Интересы" value={data.interests} />
            <FullUserOneLine name="Интересы на ВСН" value={data.vsn_interests} />
            <FullUserOneLine name="Любимые места поботать" value={data.study_places} />
            <FullUserOneLine name="Места, где хотелось бы побывать" value={data.places_to_visit} />
            <FullUserOneLine name="Любимая музыка" value={data.music} />
            <FullUserOneLine name="Любимые фильмы" value={data.favorite_movies} />
            <FullUserOneLine name="Религия" value={data.religion} />
            <FullUserOneLine name="Планы на будущее" value={data.future_plans} />
            <FullUserOneLine name="Любимый ЯП" value={data.favorite_programming_language} />
            <FullUserOneLine name="3 кумира" value={data.top_3_people} />
        </Grid2>
    )
}
