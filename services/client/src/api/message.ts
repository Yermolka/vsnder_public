import { GetMessageDto } from "../dto/message";
import { ax } from "../utils/axios";

export async function getMessages(user_id: number): Promise<Array<GetMessageDto>> {
    return await ax.get(`/user/${user_id}/messages`).then(resp => resp.data as Array<GetMessageDto>);
}

export async function getPublicMessages(user_id: number): Promise<Array<GetMessageDto>> {
    return await ax.get(`/user/${user_id}/messages/public`).then(resp => resp.data as Array<GetMessageDto>);
}

export async function postMessage(user_id: number, pub: boolean, message: string | null, file: File | null) {
    const data = new FormData();
    if (message) {
        data.append("text", message); 
    }
    if (file) {
        data.append("file", file);
    }
    data.append("public", String(pub));
    return await ax.post(`/user/${user_id}/messages`, data);
}

export async function postMessageResponse(message_id: number, message: string | null, file: File | null) {
    const data = new FormData();
    if (message) {
        data.append("text", message); 
    }
    if (file) {
        data.append("file", file);
    }
    return await ax.post(`/messages/${message_id}`, data);
}


export async function deleteMessage(message_id: number) {
    return await ax.delete(`/messages/${message_id}`);
}
