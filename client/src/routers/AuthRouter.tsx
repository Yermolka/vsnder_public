import { AuthLayout } from "../modules/auth/layout/AuthLayout";
import { LoginPage } from "../modules/auth/pages";

export const AuthRouter = {
    element: <AuthLayout />,
    children: [
        {
            path: 'login',
            element: <LoginPage />,
        },
    ],
};
