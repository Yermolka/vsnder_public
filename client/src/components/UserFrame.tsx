import { Grid2, Paper, useTheme } from "@mui/material";
import { GetUserDto } from "../dto/user";
import { Link } from "react-router-dom";

export function UserFrame(data: GetUserDto) {
    useTheme();
    
    return (
        <Paper elevation={3} style={{ padding: "10px" }}>
            <Grid2 container spacing={2}>
                 <Grid2 size={12}>
                    <Link to={`/users/${data.id}`}><h1>{data.firstName} {data.lastName}</h1></Link>
                    {data.age ? <p>Age: {data.age}</p> : null}
                 </Grid2>
            </Grid2>
        </Paper>
    )
}
