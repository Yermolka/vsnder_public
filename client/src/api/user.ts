import { ax } from "../utils/axios";
import { GetShortUserDto, GetUserDto, PostUserDto, UserChangePasswordDto } from "../dto/user"
import { AxiosError } from "axios";

export async function getUsers(page: number, limit: number, orderBy: string, orientation: string, yearOfStudy: number, status: string, query: string): Promise<{ total: number, users: Array<GetShortUserDto> }> {
    let url = `/users?page=${page}&limit=${limit}&orderBy=${orderBy}`;
    if (orientation !== "any") {
        url += `&orientation=${orientation}`;
    }
    if (yearOfStudy !== -1) {
        url += `&year_of_study=${yearOfStudy}`;
    }
    if (status !== "any") {
        url += `&status=${status}`;
    }
    if (query !== "") {
        url += `&query=${query}`;
    }

    return await ax.get(url)
        .then(res => {
            const { total, users }: { total: number, users: Array<GetShortUserDto> } = res.data;
            return { total, users };
        }, (err: AxiosError) => {
            if (err?.status === 401) { throw err }
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

export async function postUserImage(userId: number, file: File | null): Promise<string | null> {
    if (!file) {
        return null;
    }

    const data = new FormData();
    data.append("img", file);
    return await ax.post(`/users/${userId}/file`, data)
        .then(res => { return null; }, (err: AxiosError) => { return "Ошибка при загрузке аватарки"; });
}

export async function getRandomUser(): Promise<GetUserDto> {
    return await ax.get('/user/random')
        .then(res => { return res.data }, (err: AxiosError) => { return err.response?.data; });
}
