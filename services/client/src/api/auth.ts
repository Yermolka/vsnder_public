import { UserAuthDto } from "../dto/user";
import { ax } from "../utils/axios";

export async function postLogin(data: UserAuthDto) {
    return await ax.post('user/login', data);
}

export async function getLogout() {
    return await ax.get('user/logout');
}
