import { RouterProvider, createBrowserRouter } from 'react-router-dom';

import { App } from '../App';
import { AuthRouter } from './AuthRouter';

export const RootRouter = () => {
    const router = createBrowserRouter([
        {
            path: '/',
            element: <App />,
            children: [AuthRouter],
        },
    ]);

    return <RouterProvider router={router} />;
}
