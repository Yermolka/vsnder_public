import { Outlet, useNavigate } from "react-router-dom";

import { AppBar, Box } from "@mui/material";

export function AuthLayout() {
    const navigate = useNavigate();

    return (
        <Box style={{ display: 'flex' }}>
            <AppBar />
            <Outlet />
        </Box>
    )
}
