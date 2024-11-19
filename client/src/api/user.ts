import { ax } from "../utils/axios";
import { GetShortUserDto, GetUserDto, PostUserDto, UserChangePasswordDto } from "../dto/user"
import { FormEvent } from "react";
import { AxiosError } from "axios";
import { redirect } from "react-router-dom";

export async function getUsers(page: number, limit: number, orderBy: string): Promise<{ total: number, users: Array<GetShortUserDto> }> {
    const url = `/users?page=${page}&limit=${limit}&orderBy=${orderBy}`;
    return await ax.get(url)
        .then(res => {
            const { total, users }: { total: number, users: Array<GetShortUserDto> } = res.data;
            return { total, users };
        }, (err: AxiosError) => {
            return { total: 0, users: [] };
        });
}

export async function getUser(id: number): Promise<GetUserDto | null> {
    return await ax.get(`/users/${id}`)
        .then(res => { return res.data as GetUserDto; }, err => { return null; });
}

export async function postUser(data: PostUserDto): Promise<string | null> {
    return await ax.post('/user/edit', data)
        .then(res => { return null; }, (err: AxiosError) => { return err.response?.data as string; });
}

export async function postUserChangePassword(data: UserChangePasswordDto): Promise<string | null> {
    return await ax.post('/user/change_password', data)
        .then(res => { return null; }, (err: AxiosError) => { return err.response?.data as string || null; });
}

export async function getHasUserProfilePicture(userId: number) {
    return await ax.get(`/users/${userId}/file/has`)
        .then(res => { return true; }, err => { return false; });
}

export async function postUserImage(userId: number, file: File | null) {
    if (!file) {
        return null;
    }

    const data = new FormData();
    data.append("img", file);
    return await ax.post(`/users/${userId}/file`, data)
        .then(res => { return res.data; }, (err: AxiosError) => { return err.response?.data; });
}

export async function getRandomUser(): Promise<GetUserDto> {
    return await ax.get('/user/random')
        .then(res => { return res.data }, (err: AxiosError) => { return err.response?.data; });
}
