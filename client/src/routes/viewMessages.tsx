import { useEffect, useState } from "react";
import { getMessages } from "../api/message";
import { useNavigate } from "react-router-dom";
import { Box } from "@mui/material";

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
        <Box padding={5}>
            {messages.map((message, index) => { return <p key={index}>{message}</p>})}
        </Box>
    )
}
