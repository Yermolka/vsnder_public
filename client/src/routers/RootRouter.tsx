import { createBrowserRouter, RouterProvider } from "react-router-dom";
import Root from "../routes/root";
import ErrorPage from "../error-page";
import EditUser, { editUserAction, editUserLoader } from "../routes/editUser";
import { SingleUser, singleUserLoader } from "../routes/singleUser";
import { LoginPage, loginPageAction } from "../routes/loginPage";
import { Logout } from "../routes/logout";
import { ListUsers, listUsersLoader } from "../routes/listUsers";
import { ChangePassword, changePasswordAction } from "../routes/changePassword";

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
                        action: loginPageAction,
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
                        loader: listUsersLoader,
                    },
                    {
                        path: 'users/:userId',
                        element: <SingleUser />,
                        loader: singleUserLoader,
                    },
                    {
                        path: 'changePassword',
                        element: <ChangePassword />,
                        action: changePasswordAction, 
                    }
                ]
                }
            ],
        }
    ]);

    return <RouterProvider router={router} />;
}
