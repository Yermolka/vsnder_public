import { Box, Button, Grid2 } from "@mui/material";
import { redirect, useLoaderData } from "react-router-dom";
import { UserFrame } from "../components/UserFrame";
import { GetShortUserDto, GetUserDto } from "../dto/user";
import { getUsers } from "../api/user";
import { useEffect, useState } from "react";
import InfiniteScroll from "react-infinite-scroll-component";

export function ListUsers() {
    const loader = async (page: number, orderBy: string) => {
        return await getUsers(page, 32, orderBy);
    };

    const [total, setTotal] = useState(0);
    const [page, setPage] = useState(1);
    const [loadedUsers, setLoadedUsers] = useState<Array<GetShortUserDto>>([]);
    const [finished, setFinished] = useState(false);
    const [orderBy, setOrderBy] = useState("id");

    const loadMore = async () => {
        const {total, users } = await loader(page, orderBy);
        setLoadedUsers([...loadedUsers, ...users]);
        if (users.length === 0) {
            setFinished(true);
        }
        setPage(page + 1);
    };

    useEffect(() => {
        loader(page, "id").then(({ total, users }) => {
            setTotal(total);
            setLoadedUsers(users);
            setPage(page + 1);
        });
    }, []);

    useEffect(() => {
        setTotal(0);
        setLoadedUsers([]);
        setFinished(false);
        loader(1, orderBy).then(({ total, users }) => {
            setTotal(total);
            setLoadedUsers(users);
            setPage(2);
        })
    }, [orderBy])

    return (
        <Box className="list-users">
            <Button variant="contained" onClick={() => {
                if (orderBy === "id") {
                    setOrderBy("last_name");
                } else {
                    setOrderBy("id");
                }
            }}>Switch</Button>
            <InfiniteScroll
             dataLength={loadedUsers.length}
             loader={<h1><p style={{ textAlign: "center" }}>Loading...</p></h1>}
             hasMore={!finished}
             next={loadMore}>
                <Grid2 container direction="row" spacing={2} columns={{md: 12, xs: 6}} alignItems="stretch" justifyContent="center">
                    { total > 0 ? loadedUsers.map((user) => UserFrame(user)) : null}
                </Grid2>
             </InfiniteScroll>
        </Box>
    )
}
