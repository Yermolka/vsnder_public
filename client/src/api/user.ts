import { ax } from "../utils/axios";
import { GetShortUserDto, GetUserDto, PostUserDto, UserChangePasswordDto } from "../dto/user"
import { FormEvent } from "react";

export async function getUsers(page: number, limit: number, orderBy: string): Promise<{ total: number, users: Array<GetShortUserDto> }> {
    const url = `/users?page=${page}&limit=${limit}&orderBy=${orderBy}`;
    return await ax.get(url)
        .then(res => { 
            const { total, users }: {total: number, users: Array<GetShortUserDto>} = res.data;
            return { total, users};
        }, err => { return { total: 0, users: [] }; });
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

export async function postUserImage(userId: number, file: File | null) {
    if (!file) {
        return null;
    }

    const data = new FormData();
    data.append("img", file);
    const res = await ax.post(`/users/${userId}/file`, data)
        .catch(console.error);

    return res;
}
