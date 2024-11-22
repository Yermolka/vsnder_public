import { Message } from "../dto/message";
import { ax } from "../utils/axios";

export async function getMessages(user_id: number): Promise<Array<Message>> {
    return await ax.get(`/messages/${user_id}`).then(resp => resp.data as Array<Message>);
}

export async function postMessage(user_id: number, message: string) {
    return await ax.post(`/messages/${user_id}`, {text: message});
}

export async function deleteMessage(message_id: number) {
    return await ax.delete(`/messages/${message_id}`);
}
