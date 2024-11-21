import { useEffect, useState } from "react";
import { getMessages } from "../api/message";
import { useNavigate } from "react-router-dom";

export function ViewMessages() {
    const [messages, setMessages] = useState<Array<string>>([]);
    const userId = localStorage.getItem("userId") as string | null;
    const navigate = useNavigate();

    useEffect(() => {
        if (!userId) {
            navigate('/login');
        }
        getMessages(Number(userId)).then((value) => setMessages(value));
    }, [])

    return (
        <>
        {messages.map((message, index) => { return <p key={index}>{message}</p>})}
        </>
    )
}
