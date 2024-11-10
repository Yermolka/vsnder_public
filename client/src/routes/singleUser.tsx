import { useLoaderData, useNavigate } from "react-router-dom";
import { GetUserDto } from "../dto/user";
import { getUser } from "../api/user";

export function SingleUser() {
    const user = useLoaderData() as GetUserDto | undefined;
    const userId = localStorage.getItem("userId") as number | null;
    const navigate = useNavigate();

    if (user && userId && user.id === userId) {
        navigate('/edit');
    }

    return (
        <div>
            <h1>Single User</h1>
            {user ? user.firstName : "No user"}
        </div>
    );
}

export async function singleUserLoader(params: any) {
    const user = await getUser(params.userId)
    // const user = {
    //     firstName: "Max",
    //     lastName: "Hass",
    //     age: -1,
    // }
    // if (!user) {
    //     throw new Response("", {
    //         status: 404,
    //         statusText: "Not Found",
    //     });
    // }

    return user;
}
