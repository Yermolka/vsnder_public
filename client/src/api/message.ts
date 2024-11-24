import { Message } from "../dto/message";
import { ax } from "../utils/axios";

export async function getMessages(user_id: number): Promise<Array<Message>> {
    return await ax.get(`/messages/${user_id}`).then(resp => resp.data as Array<Message>);
}

export async function postMessage(user_id: number, message: string | null, file: File | null) {
    const data = new FormData();
    if (message) {
        data.append("text", message); 
    }
    if (file) {
        data.append("file", file);
    }
    return await ax.post(`/messages/${user_id}`, data);
}

export async function deleteMessage(message_id: number) {
    return await ax.delete(`/messages/${message_id}`);
}
