import { ax } from "../utils/axios";

export async function getMessages(user_id: number): Promise<Array<string>> {
    return await ax.get(`/messages/${user_id}`).then(resp => resp.data as Array<string>);
}

export async function postMessage(user_id: number, message: string) {
    return await ax.post(`/messages/${user_id}`, {text: message});
}
