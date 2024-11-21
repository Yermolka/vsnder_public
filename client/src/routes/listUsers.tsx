import { Box, Button, Divider, Grid2, InputLabel, MenuItem, Paper, Select, TextField } from "@mui/material";
import { UserFrame } from "../components/UserFrame";
import { GetShortUserDto } from "../dto/user";
import { getUser, getUsers } from "../api/user";
import { useEffect, useState } from "react";
import InfiniteScroll from "react-infinite-scroll-component";
import { redirect, useNavigate } from "react-router-dom";
import { AxiosError } from "axios";


export function ListUsers() {
    const navigate = useNavigate();
    const loader = async (page: number, orderBy: string, orientation: string, yearOfStudy: number, status: string) => {
        try {
            return await getUsers(page, 32, orderBy, orientation, yearOfStudy, status);
        } catch (e: any) {
            setError(401);
            return { total: 0, users: [] };
        }
    };

    const [error, setError] = useState<number | null>(null);
    const [total, setTotal] = useState(0);
    const [page, setPage] = useState(1);
    const [loadedUsers, setLoadedUsers] = useState<Array<GetShortUserDto>>([]);
    const [finished, setFinished] = useState(false);
    const [orderBy, setOrderBy] = useState("id");
    const [orientation, setOrientation] = useState<string>("any");
    const [yearOfStudy, setYearOfStudy] = useState<number>(-1);
    const [status, setStatus] = useState<string>("any");

    const loadMore = async () => {
        const {total, users } = await loader(page, orderBy, orientation, yearOfStudy, status);
        setLoadedUsers([...loadedUsers, ...users]);
        if (users.length === 0 || users.length === total) {
            setFinished(true);
        }
        setPage(page + 1);
    };

    useEffect(() => {
        if (error === 401) {
            navigate("/logout");
        }
        setError(null);
    }, [error]);

    useEffect(() => {
        loader(page, orderBy, orientation, yearOfStudy, status).then(({ total, users }) => {
            setTotal(total);
            setLoadedUsers(users);
            setPage(page + 1);

            if (users.length === total) {
                setFinished(true);
            }
        });
    }, []);

    useEffect(() => {
        setTotal(0);
        setLoadedUsers([]);
        setFinished(false);
        loader(1, orderBy, orientation, yearOfStudy, status).then(({ total, users }) => {
            setTotal(total);
            setLoadedUsers(users);
            setPage(2);
            if (total === 0 || users.length === total) {
                setFinished(true);
            }
        })
    }, [orderBy, orientation, yearOfStudy, status])

    const inputSxProps = {
        "& .MuiOutlinedInput-root": {
            color: "#fff",
            "&.Mui-focused": {
                "& .MuiOutlinedInput-notchedOutline": {
                    borderColor: "#fff",
                    borderWidth: "2px",
                },
            },
        },
        "& .MuiInputLabel-outlined": {
            color: "#fff",
            "&.Mui-focused": {
                color: "#fff",
            }
        }
    }

    return (
        <Box width="100%" alignContent="center" alignItems="center" justifyContent="center" justifyItems="center" >
            <Grid2 container width="80%" display="flex" flexDirection="row" spacing={2} columns={{lg: 4, md: 2, xs: 1}} paddingBottom={1}>
                <Grid2 size={1}>
                    <TextField
                        name="select-order-by"
                        label="Сортировать"
                        value={orderBy}
                        select
                        onChange={(e) => setOrderBy(e.target.value)}
                        sx={inputSxProps}
                        fullWidth>
                        <MenuItem value="id">По умолчанию</MenuItem>
                        <MenuItem value="first_name">По имени</MenuItem>
                        <MenuItem value="last_name">По фамилии</MenuItem>
                        <MenuItem value="age">По возрасту</MenuItem>
                        <MenuItem value="orientation">По направлению</MenuItem>
                        <MenuItem value="age_of_study">По курсу</MenuItem>
                    </TextField>
                </Grid2>
                <Grid2 size={1}>
                    <TextField
                        name="select-orientation"
                        label="Направление"
                        value={orientation}
                        onChange={(e) => setOrientation(e.target.value)}
                        select
                        sx={inputSxProps}
                        fullWidth>
                        <MenuItem value="any">Любое</MenuItem>
                        <MenuItem value="Психология">Психология</MenuItem>
                        <MenuItem value="Социология">Социология</MenuItem>
                        <MenuItem value="Политология">Политология</MenuItem>
                        <MenuItem value="ГМУ">ГМУ</MenuItem>
                    </TextField>
                </Grid2>
                <Grid2 size={1}>
                    <TextField
                        name="select-year-of-study"
                        label="Курс"
                        value={yearOfStudy}
                        onChange={(e) => setYearOfStudy(Number(e.target.value))}
                        select 
                        sx={inputSxProps}
                        fullWidth>
                        <MenuItem value="-1">Любой</MenuItem>
                        <MenuItem value="1">1</MenuItem>
                        <MenuItem value="2">2</MenuItem>
                        <MenuItem value="3">3</MenuItem>
                        <MenuItem value="4">4</MenuItem>
                    </TextField>
                </Grid2>
                <Grid2 size={1}>
                    <TextField
                        name="select-status"
                        label="Семейное положение"
                        value={status}
                        onChange={(e) => setStatus(e.target.value)}
                        select 
                        sx={inputSxProps}
                        fullWidth>
                        <MenuItem value="any">Любое</MenuItem>
                        <MenuItem value="Замужем/Женат">Замужем/Женат</MenuItem>
                        <MenuItem value="В отношениях">В отношениях</MenuItem>
                        <MenuItem value="Схожу на свидание">Схожу на свидание</MenuItem>
                        <MenuItem value="Чиллю соло">Чиллю соло</MenuItem>
                    </TextField>
                </Grid2>
            </Grid2>
            <Divider variant="middle" flexItem />
            <InfiniteScroll
             dataLength={loadedUsers.length}
             loader={<h1><p style={{ textAlign: "center" }}>Загружаем еще...</p></h1>}
             hasMore={!finished}
             next={loadMore}>
                <Grid2 sx={{ width: "100vw"}} container direction="row" spacing={2} columns={{md: 12, xs: 6}} alignItems="center" alignContent="center" justifyItems="center" justifyContent="center">
                    { total > 0 ? loadedUsers.map((user) => UserFrame(user)) : null}
                </Grid2>
             </InfiniteScroll>
        </Box>
    )
}
