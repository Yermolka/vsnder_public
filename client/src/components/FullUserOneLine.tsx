import { Divider, Grid2, Typography } from "@mui/material";

export function FullUserOneLine(props: {name: string, value: number | string | undefined}) {
    return (
        <>
            <Grid2 size={3}>
                <Typography>{props.name}:</Typography>
            </Grid2>
            <Grid2 size={3}>
                <Typography>{props.value || "Не указано"}</Typography>
            </Grid2>
            <Grid2 size={6}>
                <Divider variant="middle" />
            </Grid2>
        </>
    )
}
