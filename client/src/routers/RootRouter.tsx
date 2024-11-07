import { createBrowserRouter, RouterProvider } from "react-router-dom";
import Root, { rootLoader } from "../routes/root";
import ErrorPage from "../error-page";
import EditUser, { editUserAction, editUserLoader } from "../routes/editUser";
import { SingleUser, singleUserLoader } from "../routes/singleUser";

export const RootRouter = () => {
    const router = createBrowserRouter([
        {
            path: '/',
            element: <Root />,
            errorElement: <ErrorPage />,
            loader: rootLoader,
            children: [
                // {
                //     path: 'login',
                //     // element: <LoginPage />,
                // },
                {
                    path: 'user',
                    element: <EditUser />,
                    action: editUserAction,
                    loader: editUserLoader,
                },
                {
                    path: 'users',
                },
                {
                    path: 'user/:userId',
                    element: <SingleUser />,
                    loader: singleUserLoader,
                }
            ],
        }
    ]);

    return <RouterProvider router={router} />;
}
