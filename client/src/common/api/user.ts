import { PostUserDto } from "../dto/user";
import { createUserFromDto } from "../models/user";

import { ax } from "../axios";

export async function getUser() {
    const res = await ax.get('/user');

    return createUserFromDto(res.data);
}
