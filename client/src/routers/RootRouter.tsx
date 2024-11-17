import { createBrowserRouter, RouterProvider } from "react-router-dom";
import Root from "../routes/root";
import ErrorPage from "../error-page";
import EditUser, { editUserLoader } from "../routes/editUser";
import { SingleUser, singleUserLoader, singleUserRouletteLoader } from "../routes/singleUser";
import { LoginPage } from "../routes/loginPage";
import { Logout } from "../routes/logout";
import { ListUsers } from "../routes/listUsers";
import { ChangePassword } from "../routes/changePassword";

export const RootRouter = () => {
    const router = createBrowserRouter([
        {
            path: '/',
            element: <Root />,
            errorElement: <ErrorPage />,
            children: [
                {
                    errorElement: <ErrorPage />,
                    children:[
                    {
                        path: 'login',
                        element: <LoginPage />,
                    },
                    {
                        path: 'logout',
                        element: <Logout />,
                    },
                    {
                        path: 'edit',
                        element: <EditUser />,
                        loader: editUserLoader,
                    },
                    {
                        path: 'users',
                        element: <ListUsers />,
                    },
                    {
                        path: 'users/:userId',
                        element: <SingleUser />,
                        loader: singleUserLoader,
                    },
                    {
                        path: 'changePassword',
                        element: <ChangePassword />,
                    },
                    {
                        path: 'roulette',
                        element: <SingleUser />,
                        loader: singleUserRouletteLoader,
                    }
                ]
                }
            ],
        }
    ]);

    return <RouterProvider router={router} />;
}
