import { AxiosError } from "axios";
import { useEffect } from "react";
import { useNavigate, useRouteError } from "react-router-dom";

export default function ErrorPage() {
    const error: any = useRouteError()
    const navigate = useNavigate();

    useEffect(() => {
        if (error.status === 401) {
            navigate("/logout");
        }
    }, [error]);

    return (
        <div id="error-page">
            <h1>Ууупс!</h1>
            <p>Произошла ошибка</p>
            <p>
                <i>{error.statusText || error.message}</i>
            </p>
            <a href="/">На главную</a>
        </div>
    )
}
