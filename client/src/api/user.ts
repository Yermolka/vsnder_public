import { ax } from "../utils/axios";
import { GetShortUserDto, GetUserDto, PostUserDto, UserChangePasswordDto } from "../dto/user"

export async function getUsers(): Promise<Array<GetShortUserDto>> {
    return await ax.get('/users')
        .then(res => { return res.data as Array<GetShortUserDto>; }, err => { return []; });
}

export async function getUser(id: number): Promise<GetUserDto | null> {
    return await ax.get(`/users/${id}`)
        .then(res => { return res.data as GetUserDto; }, err => { return null; });
}

export async function postUser(data: PostUserDto): Promise<number | string> {
    return await ax.post('/user/edit', data)
        .then(res => { return res.data.userId; }, err => { return err.data; });
}

export async function postUserChangePassword(data: UserChangePasswordDto) {
    return await ax.post('/user/change_password', data)
        .then(res => { return res.data.userId; }, err => { return err.data; });
}

export async function getHasUserProfilePicture(userId: number) {
    const res = await ax.get(`/users/${userId}/file/has`)
        .then(res => { return true; }, err => { return false; });

    return res;
}
