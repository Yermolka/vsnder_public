import { useLoaderData, useNavigate } from "react-router-dom";
import { GetUserDto } from "../dto/user";
import { getUser } from "../api/user";
import { useEffect } from "react";
import { FullUserFrame } from "../components/FullUserFrame";

export function SingleUser() {
    const user = useLoaderData() as GetUserDto | undefined;
    const userId = localStorage.getItem("userId") as string | null;
    const navigate = useNavigate();

    useEffect(() => {
        if (user && userId && user.id === parseInt(userId)) {
            navigate('/edit');
        }
    }, [user, userId]) 

    return (
        <div>
            {user ? (FullUserFrame(user)) : <h1>No user</h1>}
        </div>
    );
}

export async function singleUserLoader({ params }: any) {
    console.log(params);

    const user = await getUser(params.userId)
    if (user.status === 200) {
        return user.data;
    }

    return null;
}
