import { Outlet, useMatch, useNavigate, useNavigation } from "react-router-dom";
import { Box, Skeleton } from "@mui/material";
import { useEffect } from "react";
import { VSNBreadcrumbs } from "../components/Breadcrumbs";
import { ErrorBoundary } from "react-error-boundary";
import ErrorFallback from "../components/ErrorFallback";

export default function Root() {
    const navigation = useNavigation();
    const navigate = useNavigate();
    const appMatch = useMatch({ path: '/', end: true });

    const userId = localStorage.getItem("userId");
    useEffect(() => {
        if (appMatch) {
            if (userId === null) {
                return navigate('/login');
            } else {
                return navigate('/users');
            };
        } 
    }, [appMatch]);

    return (
        <ErrorBoundary fallback={<div>ERROR</div>}>
            <div className="div-header">
                {userId === null ? "" : <VSNBreadcrumbs />}
                <h1>VSNder</h1>
            </div>
            {navigation.state === "loading" ? <Skeleton /> : null }
            
            <div id="detail">
                <Box width="100vw" alignContent="center" justifyContent="center" alignItems="center" justifyItems="center">
                    <Outlet />
                </Box>
            </div>
        </ErrorBoundary>
    );
}
