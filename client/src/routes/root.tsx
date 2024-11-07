import { Link, Outlet, useLoaderData, useNavigation } from "react-router-dom";
import { getUsers } from "../api/user";
import { CircularProgress } from "@mui/material";

export default function Root() {
    const users : Array<any> = useLoaderData() as Array<any>;
    const navigation = useNavigation();

    return (
        <>
        <nav>
            <ul>
                <li>
                    <Link to={`/`}>На главную</Link>
                </li>
                <li>
                    <Link to={`/user`}>Изменить данные</Link>
                </li>
                <li>
                    <Link to={`/users`}>Смотреть всех</Link>
                </li>
            </ul>
        </nav>
        <h1>Hello World</h1>
        {navigation.state === "loading" ? "loading" : null }
        {users.length ? (
            <ul>
                {users.map((user: any) => (
                    <li key={user.id}>
                        <Link to={`user/${user.id}`}>
                            {user.firstName} {user.lastName}
                        </Link>
                    </li>
                ))}
            </ul>
            ) : <p>Нет пользователей</p>
        }
        <div id="detail">
            <Outlet />
        </div>
        </>
    );
}

export async function rootLoader() {
    const users = await getUsers();
    await new Promise(resolve => setTimeout(resolve, 1000));
    return users;
}
