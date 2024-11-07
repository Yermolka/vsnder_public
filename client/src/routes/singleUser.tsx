import { useLoaderData } from "react-router-dom";
// import { getUser } from "../api/user";

export function SingleUser() {
    const user: any = useLoaderData();

    return (
        <div>
            <h1>Single User</h1>
            {user ? user.firstName : "No user"}
        </div>
    );
}

export async function singleUserLoader(params: any) {
    // const user = await getUser(params.userId)
    const user = {
        firstName: "Max",
        lastName: "Hass",
        age: -1,
    }

    return user;
}
