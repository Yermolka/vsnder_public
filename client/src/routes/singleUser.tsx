import { Link, useLoaderData, useNavigate } from "react-router-dom";
import { GetUserDto } from "../dto/user";
import { getRandomUser, getUser } from "../api/user";
import { useEffect } from "react";
import { FullUserFrame } from "../components/FullUserFrame";
import dayjs from "dayjs";
import { Button } from "@mui/material";
import { AnonMessageForm } from "../components/AnonMessageForm";

export function SingleUser() {
    const user = useLoaderData() as GetUserDto | null;
    const userId = localStorage.getItem("userId") as string | null;
    const navigate = useNavigate();

    useEffect(() => {
        if (user && userId && user.id === parseInt(userId)) {
            navigate('/edit');
        }
    }, [user, userId])

    return (
        <div style={{alignContent: "center", alignItems: "center", justifyContent: "center", justifyItems: "center"}}>
            {user ? <h1 style={{ textAlign: "center" }}>{user.first_name} {user.last_name}</h1> : null}
            {user && user.birth_stamp && user.birth_city ? <Link to={createCultUrl(user)} target="_blank" rel="noreferrer"><Button fullWidth variant="contained" size="large">НАТАЛЬНАЯ КАРТА</Button></Link> : null}
            {user ? (FullUserFrame(user)) : <h1>No user</h1>}
            {user ? (AnonMessageForm(user.id)) : null}
        </div>
    );
}

export async function singleUserLoader({ params }: any): Promise<GetUserDto | null> {
    return await getUser(params.userId)
}

function createCultUrl(user: GetUserDto) {
    const parsedDate = dayjs(user.birth_stamp);
    return `http://geocult.ru/natalnaya-karta-onlayn-raschet?` +
        `fn=${user.first_name}&fd=${parsedDate.date()}&fm=${parsedDate.month() + 1}&fy=${parsedDate.year()}` +
        `&fh=${parsedDate.hour()}&fmn=${parsedDate.minute()}&c1=${user.birth_city}&lt=55.7522&ln=37.6155&hs=P&sb=1`
}

export async function singleUserRouletteLoader(): Promise<GetUserDto> {
    return await getRandomUser();
}
