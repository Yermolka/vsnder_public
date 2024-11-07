import { useRouteError } from "react-router-dom";

export default function ErrorPage() {
    const error: any = useRouteError()
    console.log(error);

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
