import { Link, useLoaderData, useNavigate } from "react-router-dom";
import { GetUserDto } from "../dto/user";
import { getCoords, getRandomUser, getUser } from "../api/user";
import { useEffect, useState } from "react";
import { FullUserFrame } from "../components/FullUserFrame";
import dayjs from "dayjs";
import { Button } from "@mui/material";
import { AnonMessageForm } from "../components/AnonMessageForm";

export function SingleUser() {
    const user = useLoaderData() as GetUserDto | null;
    const userId = localStorage.getItem("userId") as string | null;
    const [isSelf, setIsSelf] = useState(false);
    const [coords, setCoords] = useState<{lat: number, lng: number} | null>(null);
    const [astroUrl, setAstroUrl] = useState<string | null>(null);
     

    useEffect(() => {
        if (user && userId && user.id === parseInt(userId)) {
            setIsSelf(true);
        }
    }, [user, userId])

    useEffect(() => {
        if (user && user.birth_city) {
            getCoords(user.birth_city).then(setCoords);
        }
    }, [user])

    useEffect(() => {
        if (user && user.birth_city && userId) {
            getUser(Number(userId)).then(value => {
                if (value && value.birth_city && value.birth_stamp) {
                    setAstroUrl(createAstroUrl(user, value));
                }
            })
        }
    }, [user, userId])

    return (
        <div style={{ alignContent: "center", alignItems: "center", justifyContent: "center", justifyItems: "center" }}>
            {isSelf && user ? <Link to={`/edit`}><Button fullWidth variant="contained" size="large">Редактировать</Button></Link> : null}
            {user ? <h1 style={{ textAlign: "center" }}>{user.first_name} {user.last_name}</h1> : null}
            {user && user.birth_stamp && coords ? <Link to={createCultUrl(user, coords)} target="_blank" rel="noreferrer"><Button fullWidth variant="contained" size="large">НАТАЛЬНАЯ КАРТА</Button></Link> : null}
            {astroUrl ? <Link style={{paddingTop: 3}} to={astroUrl} target="_blank" rel="noreferrer"><Button fullWidth variant="contained" size="large">Совместимость с тобой</Button></Link> : null}
            {user ? (FullUserFrame(user)) : <h1>No user</h1>}
            {user ? (AnonMessageForm(user.id)) : null}
        </div>
    );
}

export async function singleUserLoader({ params }: any): Promise<GetUserDto | null> {
    return await getUser(params.userId)
}

function createCultUrl(user: GetUserDto, coords: {lng: number, lat: number}) {
    const parsedDate = dayjs(user.birth_stamp);
    return `http://geocult.ru/natalnaya-karta-onlayn-raschet?` +
        `fn=${user.first_name}&fd=${parsedDate.date()}&fm=${parsedDate.month() + 1}&fy=${parsedDate.year()}` +
        `&fh=${parsedDate.hour()}&fmn=${parsedDate.minute()}&c1=${user.birth_city}&lt=${coords.lat}&ln=${coords.lng}&hs=P&sb=1`
}

function createAstroUrl(user: GetUserDto, zhena: GetUserDto) {
    const first = dayjs(user.birth_stamp);
    const second = dayjs(zhena.birth_stamp);

    return `https://ru.astro-seek.com/vychislit-goroskop-sovmestimosti/?send_calculation=1& \
    muz_narozeni_den=${first.date()}&muz_narozeni_mesic=${first.month() + 1}&muz_narozeni_rok=${first.year()}\
    &muz_narozeni_hodina=${first.hour()}&muz_narozeni_minuta=${first.minute()}&muz_narozeni_city=${user.birth_city}\
    &muz_narozeni_stat_hidden=RU&muz_narozeni_podstat_kratky_hidden=\
    &muz_narozeni_sirka_stupne=55&muz_narozeni_sirka_minuty=45&muz_narozeni_sirka_smer=0&muz_narozeni_delka_stupne=37&muz_narozeni_delka_minuty=37&muz_narozeni_delka_smer=0\
    &muz_narozeni_timezone_form=auto&muz_narozeni_timezone_dst_form=auto&send_calculation=1\
    &zena_narozeni_den=${second.date()}&zena_narozeni_mesic=${second.month() + 1}&zena_narozeni_rok=${second.year()}\
    &zena_narozeni_hodina=${second.hour()}&zena_narozeni_minuta=${second.minute()}&zena_narozeni_city=${zhena.birth_city}\
    &zena_narozeni_stat_hidden=RU&zena_narozeni_podstat_kratky_hidden=&zena_narozeni_sirka_stupne=55&zena_narozeni_sirka_minuty=45&zena_narozeni_sirka_smer=0&zena_narozeni_delka_stupne=37&zena_narozeni_delka_minuty=37&zena_narozeni_delka_smer=0\
    &zena_narozeni_timezone_form=auto&zena_narozeni_timezone_dst_form=auto&house_system=placidus&uhel_orbis=#tabs_redraw`
}

export async function singleUserRouletteLoader(): Promise<GetUserDto> {
    return await getRandomUser();
}
