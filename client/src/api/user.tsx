import { PostUserDto } from "../dto/user"

export async function getUsers() {
    return [
        {
            id: 1,
            firstName: "Andrey",
            lastName: "Yermoshin",
            age: 24,
        },
        {
            id: 2,
            firstName: "Max",
            lastName: "Hass",
            age: 0,
        },
    ]
}

export async function postUser(data: PostUserDto) {
    return data.age ? data.age : 0;
}
