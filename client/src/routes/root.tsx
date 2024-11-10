import { Link, Outlet, useLoaderData, useMatch, useNavigate, useNavigation } from "react-router-dom";
import { getUsers } from "../api/user";
import { Skeleton } from "@mui/material";
import { useEffect } from "react";
import { VSNBreadcrumbs } from "../components/Breadcrumbs";

export default function Root() {
    const navigation = useNavigation();
    const navigate = useNavigate();
    const appMatch = useMatch({ path: '/', end: true });

    const userId = localStorage.getItem("userId");
    useEffect(() => {
        if (appMatch) {
            console.log(`index: ${userId}`);
            if (userId === null) {
                return navigate('/login');
            } else {
                return navigate('/users');
            };
        } 
    }, [appMatch]);

    return (
        <>
            <div className="div-header">
                {userId === null ? "" : <VSNBreadcrumbs />}
                <h1>VSNder</h1>
            </div>
            {navigation.state === "loading" ? <Skeleton /> : null }
            
            <div id="detail">
                <Outlet />
            </div>
        </>
    );
}
