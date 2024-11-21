import { Button, Grid2, TextField } from "@mui/material";
import { Form, Formik } from "formik";
import * as yup from "yup";
import { postMessage } from "../api/message";
import { useState } from "react";

export function AnonMessageForm(receiver_id: number) {
    const [formText, setFormText] = useState<string | null>(null);

    const initialValues = {
        text: '',
    }

    const validationSchema = yup.object().shape({
        text: yup.string().required().max(500),
    })

    return (
        <Formik 
        initialValues={initialValues} 
        validationSchema={validationSchema}
        onSubmit={(values: {text: string}, { setSubmitting }) => {
            console.log(values.text);
            postMessage(receiver_id, values.text).then(() => {
                setFormText("Отправлено!");
            })
            setSubmitting(false);
        }}>
            {props => 
            <Form>
                <Grid2>
                    <TextField 
                    multiline
                    rows={4}
                    name="text"
                    label="Оставить анонимное сообщение"
                    value={props.values.text}
                    error={Boolean(props.errors.text)}
                    helperText={props.errors.text} 
                    onChange={props.handleChange}/>
                    <Button type="submit" variant="contained">Отправить</Button>
                    {formText && <p>{formText}</p> }
                </Grid2>
            </Form>
            }

        </Formik>
    )
}
