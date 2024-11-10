import { ax } from "../utils/axios";
import { PostUserDto, UserChangePasswordDto } from "../dto/user"

export async function getUsers() {
    return await ax.get('/users');
}

export async function getUser(id: number) {
    return await ax.get(`/users/${id}`);
}

export async function postUser(data: PostUserDto) {
    return await ax.post('/user/edit', data);
}

export async function postUserChangePassword(data: UserChangePasswordDto) {
    return await ax.post('/user/change_password', data);
}
