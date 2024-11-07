import { Form, redirect, useLoaderData } from "react-router-dom";
import { postUser } from "../api/user";

export default function EditUser() {
    const user: any = useLoaderData();

    return (
        <div id="edit-user">
            
            <div>
                <Form
                  method="post"
                  id="edit-user-form"
                  >
                    <h1>{user.firstName} {user.lastName}</h1>
                    <input type="number" id="age" name="age" defaultValue={user.age}></input>
                    <button type="submit">Сохранить</button>
                  </Form>
            </div>
        </div>
    )
}

export async function editUserAction({ request, params }: any) {
    const formData = await request.formData();
    const updates = Object.fromEntries(formData);

    console.log(updates);

    await postUser(updates);
    return redirect(`/`);
}

export async function editUserLoader({ params } : any) {
    // const user = await getUser(params.userId)
    const user = {
        firstName: "Andrey",
        lastName: params.userId,
        age: 12,
    }

    return user;
}
