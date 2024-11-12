import { Box, Grid2 } from "@mui/material";
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

    const loadMore = async () => {
        const {total, users } = await loader(page, "id");
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

    return (
        <Box className="list-users">
            <InfiniteScroll
             dataLength={loadedUsers.length}
             loader={<h1>Loading...</h1>}
             hasMore={!finished}
             endMessage={<p style={{ textAlign: "center" }}>That's all!</p>}
             next={loadMore}>
                <Grid2 container direction="row" spacing={2} columns={{md: 12, xs: 6}} alignItems="stretch" justifyContent="center">
                    { total > 0 ? loadedUsers.map((user) => UserFrame(user)) : null}
                </Grid2>
             </InfiniteScroll>
        </Box>
    )
}
