import { Button, Grid2, Input, TextField } from "@mui/material";
import { Form, Formik } from "formik";
import * as yup from "yup";
import { postMessage } from "../api/message";
import { ChangeEvent, useState } from "react";

export function AnonMessageForm(receiver_id: number) {
    const [formText, setFormText] = useState<string | null>(null);
    const [file, setFile] = useState<File | null>(null);

    const initialValues = {
        text: '',
    }

    const validationSchema = yup.object().shape({
        text: yup.string().max(500),
    })

    const handleFile = (file: File | null) => {
        setFile(file);
    }

    const handleFileChange = (event: ChangeEvent<HTMLInputElement>) => {
        if (event.target.files && event.target.files.length > 0) {
            handleFile(event.target.files[0]);
        } else {
            handleFile(null);
        }
    }

    return (
        <Formik 
        initialValues={initialValues} 
        validationSchema={validationSchema}
        onSubmit={(values: {text: string}, { setSubmitting, resetForm }) => {
            if (values.text.length > 0 || file) {
                postMessage(receiver_id, values.text, file).then(() => {
                    resetForm();
                    handleFile(null);
                })
            }
            setSubmitting(false);
        }}>
            {props => 
            <Form>
                <Grid2 container columns={1} spacing={2} alignContent="center" alignItems="center" justifyContent="center" justifyItems="center">
                    <Grid2 size={1}>
                        <TextField 
                        multiline
                        rows={4}
                        name="text"
                        label="Оставить анонимное сообщение"
                        value={props.values.text}
                        error={Boolean(props.errors.text)}
                        helperText={props.errors.text} 
                        onChange={(e) => {
                            props.handleChange(e);
                        }}
                        sx={{
                            "& .MuiOutlinedInput-root": {
                                color: "#fff",
                                "&.Mui-focused": {
                                    "& .MuiOutlinedInput-notchedOutline": {
                                        borderColor: "#fff",
                                        borderWidth: "2px",
                                    },
                                },
                            },
                            "& .MuiInputLabel-outlined": {
                                color: "#fff",
                                "&.Mui-focused": {
                                    color: "#fff",
                                }
                            }
                        }} 
                        fullWidth/>
                    </Grid2>
                    <Grid2 size={1}>
                        <Input type="file" name="img" id="img" onChange={handleFileChange} />
                    </Grid2>
                    <Grid2 size={1}>
                        <Button fullWidth type="submit" variant="contained">Отправить</Button>
                        {formText && <p>{formText}</p> }
                    </Grid2>
                </Grid2>
            </Form>
            }

        </Formik>
    )
}
