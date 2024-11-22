import { useEffect, useState } from "react";
import { deleteMessage, getMessages } from "../api/message";
import { useNavigate } from "react-router-dom";
import { Box, Button, Grid2 } from "@mui/material";
import { Message } from "../dto/message";


export function ViewMessages() {
    const [messages, setMessages] = useState<Array<Message>>([]);
    const userId = localStorage.getItem("userId") as string | null;
    const navigate = useNavigate();

    useEffect(() => {
        if (!userId) {
            navigate('/login');
        }
        getMessages(Number(userId)).then((value) => setMessages(value));
    }, [])

    const btnHandler = (id: number) => {
        deleteMessage(id).then((value) => {
            setMessages(messages.filter((value, index, array) => value.id != id));
        })
    }

    return (
        <Box padding={5}>
            <Grid2 container spacing={2} columns={2} direction="column" alignItems="end" alignContent="center" justifyItems="center" justifyContent="center">
                {messages.map((message, index) => { 
                    return (
                        <div key={message.id}>
                            <Grid2 size={2}><p>{message.text}<Button sx={{marginLeft: 5}} variant="contained" onClick={(e) => btnHandler(message.id)}>Удалить</Button></p>
                            </Grid2>
                        </div>
                    )
                })}
            </Grid2>
        </Box>
    )
}
