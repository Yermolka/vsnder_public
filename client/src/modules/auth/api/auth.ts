import { LoginDto } from "../../../common/dto/auth";
import { ax } from "../../../common/axios";

export async function login(data: LoginDto) {
    const res = await ax.post('/user/login', data);

    return res.data;
}

export async function logout() {
    const res = await ax.get('/user/logout');

    return res.data;
}
