import { Link, Outlet, useLoaderData, useMatch, useNavigate, useNavigation } from "react-router-dom";
import { getUsers } from "../api/user";
import { CircularProgress } from "@mui/material";
import { useEffect } from "react";

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
                {userId === null ? "" : <nav>
                    <ul className="header-nav">
                        <li>
                            <Link to={`/users`}>Смотреть всех</Link>
                        </li>
                        <li>
                            <Link to={`/edit`}>Изменить данные</Link>
                        </li>
                        <li>
                            <Link to={`/changePassword`}>Изменить пароль</Link>
                        </li>
                        <li>
                            <Link to={`/users/1`}>Крутануть рулетку!</Link>
                        </li>
                        <li>
                            <Link to={`/logout`}>Выйти</Link>
                        </li>
                    </ul>
                </nav>}
                <h1>VSNder</h1>
            </div>
            {navigation.state === "loading" ? "loading" : null }
            
            <div id="detail">
                <Outlet />
            </div>
        </>
    );
}
