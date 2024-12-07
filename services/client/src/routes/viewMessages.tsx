import { useEffect, useState } from "react";
import { deleteMessage, getMessages } from "../api/message";
import { useNavigate } from "react-router-dom";
import { Box, Button, Grid2 } from "@mui/material";
import { GetMessageDto } from "../dto/message";


export function ViewMessages() {
    const [messages, setMessages] = useState<Array<GetMessageDto>>([]);
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
            setMessages(messages.filter((value, index, array) => value.id !== id));
        })
    }

    return (
        <Box padding={5}>
            <Grid2 container spacing={2} columns={3} direction="column" alignItems="center" alignContent="center" justifyItems="center" justifyContent="center">
                {messages.map((message, index) => { 
                    return (
                        <div key={message.id}>
                            {message.file_id ? 
                                (<Grid2 size={2}>
                                    <img src={`/api/file/${message.file_id}`} alt={"Пикча"} width={150} height={150} />
                                </Grid2>) : null}
                            <Grid2 size={(message.file_id ? 1 : 3)}>
                                <p>{message.text}<Button sx={{marginLeft: 5}} variant="contained" onClick={(e) => btnHandler(message.id)}>Удалить</Button></p>
                            </Grid2>
                        </div>
                    )
                })}
            </Grid2>
        </Box>
    )
}
