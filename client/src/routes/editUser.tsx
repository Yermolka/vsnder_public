import { redirect, useLoaderData, useNavigate } from "react-router-dom";
import { getUser, postUser, postUserImage } from "../api/user";
import { Formik, Form } from "formik";
import { editUserValidationSchema } from "../utils/validation";
import { Button, Grid2, Input, InputLabel, MenuItem, Paper, Select, TextField, Typography } from "@mui/material";
import { GetUserDto, PostUserDto, postUserFromGetUserDto } from "../dto/user";
import { Form as ReactForm } from "react-router-dom";
import { ChangeEvent, useState } from "react";
import { DateTimePicker } from "@mui/x-date-pickers";
import dayjs from "dayjs";
import { ProfilePicture } from "../components/ProfilePicture";

export default function EditUser() {
    const loaderData = useLoaderData() as GetUserDto;
    const user = postUserFromGetUserDto(loaderData);
    const [file, setFile] = useState<File | null>(null);
    const [postMsg, setPostMsg] = useState<string | null>(null);
    const [postFileMsg, setPostFileMsg] = useState<string | null>(null);

    const inputSxProps = {
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
    }

    const handleFile = (file: File) => {
        if (!file) return;

        setFile(file);
    }
    const handleFileChange = (event: ChangeEvent<HTMLInputElement>) => {
        if (event.target.files && event.target.files.length > 0) {
            handleFile(event.target.files[0]);
        }
    }

    return (
        <Formik
            initialValues={user}
            validationSchema={editUserValidationSchema}
            onSubmit={(values, { setSubmitting }) => {
                editUserAction(values).then((value: string | null) => {
                    if (!value) {
                        setPostMsg("Изменения сохранены");
                    } else {
                        setPostMsg(value);
                    }
                });
                
                if (file) {
                    postUserImage(loaderData.id, file).then((value: string | null) => {
                        if (!value) {
                            setPostFileMsg("Аватарка обновлена");
                        } else {
                            setPostFileMsg(value);
                        }
                    });
                }
                setSubmitting(false);
            }}>
            {props =>
                // <Paper sx={{ borderRadius: 10, maxWidth: {lg: "60%", md: "60%", xs: "90%"} }} elevation={3} style={{ padding: "25px", margin: "10px" }}>
                    <Form className="edit-user-form">
                        <Grid2 container maxWidth="80%" spacing={2} columns={3} alignItems="center" display="flex" justifyContent="center">
                            <Grid2 size={3}>
                                <ProfilePicture userId={loaderData.id} hasAvatar={loaderData.has_avatar} size={200} />
                            </Grid2>
                            <Grid2 size={3}>
                                <Typography>Аватарка: <Input type="file" name="img" id="img" onChange={handleFileChange} /></Typography>
                            </Grid2>
                            <Grid2 size={3}>
                                <TextField
                                    type="number"
                                    name="age"
                                    label="Возраст"
                                    value={props.values.age}
                                    onChange={props.handleChange}
                                    fullWidth
                                    sx={inputSxProps}/>
                            </Grid2>
                            <Grid2 size={3}>
                                <TextField
                                    type="text"
                                    variant="outlined"
                                    name="interests"
                                    label="Увлечения"
                                    value={props.values.interests}
                                    onChange={props.handleChange}
                                    fullWidth 
                                    sx={inputSxProps}
                                    />
                            </Grid2>
                            <Grid2 size={3}>
                                <TextField
                                    type="text"
                                    name="vsn_interests"
                                    label="Увлечения на ВСН"
                                    value={props.values.vsn_interests}
                                    onChange={props.handleChange}
                                    fullWidth 
                                    sx={inputSxProps}/>
                            </Grid2>
                            <Grid2 size={3}>
                                <TextField
                                    type="text"
                                    name="places_to_visit"
                                    label="Места, которые ты хочешь посетить"
                                    value={props.values.places_to_visit}
                                    onChange={props.handleChange}
                                    fullWidth 
                                    sx={inputSxProps}/>
                            </Grid2>
                            <Grid2 size={3}>
                                <TextField
                                    type="text"
                                    name="study_places"
                                    label="Где ты ботаешь"
                                    value={props.values.study_places}
                                    onChange={props.handleChange}
                                    fullWidth 
                                    sx={inputSxProps}/>
                            </Grid2>
                            <Grid2 size={3}>
                                <TextField
                                    type="text"
                                    name="music"
                                    label="Любимая музыка"
                                    value={props.values.music}
                                    onChange={props.handleChange}
                                    fullWidth
                                    sx={inputSxProps} />
                            </Grid2>
                            <Grid2 size={3}>
                                <TextField
                                    type="text"
                                    name="favorite_movies"
                                    label="Любимые фильмы"
                                    value={props.values.favorite_movies}
                                    onChange={props.handleChange}
                                    fullWidth
                                    sx={inputSxProps} />
                            </Grid2>
                            <Grid2 size={3}>
                                <TextField
                                    type="text"
                                    name="religion"
                                    label="Религия"
                                    value={props.values.religion}
                                    onChange={props.handleChange}
                                    fullWidth
                                    sx={inputSxProps} />
                            </Grid2>
                            <Grid2 size={3}>
                                <TextField
                                    label="Семейное положение"
                                    name="status"
                                    value={props.values.status}
                                    onChange={props.handleChange}
                                    fullWidth
                                    error={Boolean(props.errors.status)}
                                    sx={inputSxProps}
                                    select>
                                    <MenuItem value="Замужем/Женат">Замужем/Женат</MenuItem>
                                    <MenuItem value="В отношениях">В отношениях</MenuItem>
                                    <MenuItem value="Схожу на свидание">Схожу на свидание</MenuItem>
                                    <MenuItem value="Чиллю соло">Чиллю соло</MenuItem>
                                </TextField>
                            </Grid2>
                            <Grid2 size={3}>
                                <TextField
                                    type="text"
                                    name="future_plans"
                                    label="Планы на будущее"
                                    value={props.values.future_plans}
                                    onChange={props.handleChange}
                                    fullWidth 
                                    sx={inputSxProps}/>
                            </Grid2>
                            <Grid2 size={3}>
                                <TextField
                                    type="text"
                                    name="family_opinion"
                                    label="Отношение к семье"
                                    value={props.values.family_opinion}
                                    onChange={props.handleChange}
                                    fullWidth
                                    sx={inputSxProps} />
                            </Grid2>
                            <Grid2 size={3}>
                                <TextField
                                    type="text"
                                    name="favorite_programming_language"
                                    label="Любимый язык программирования"
                                    value={props.values.favorite_programming_language}
                                    onChange={props.handleChange}
                                    fullWidth 
                                    sx={inputSxProps}/>
                            </Grid2>
                            <Grid2 size={3}>
                                <TextField
                                    type="text"
                                    name="top_3_people"
                                    label="Топ 3 персоны"
                                    value={props.values.top_3_people}
                                    onChange={props.handleChange}
                                    fullWidth
                                    sx={inputSxProps} />
                            </Grid2>
                            <Grid2 size={3}>
                                <TextField
                                    type="text"
                                    name="birth_city"
                                    label="Город рождения"
                                    value={props.values.birth_city}
                                    onChange={props.handleChange}
                                    fullWidth 
                                    sx={inputSxProps}/>
                            </Grid2>
                            <Grid2 size={3}>
                                <TextField
                                    name="smoking"
                                    label="Отношение к курению"
                                    value={props.values.smoking || "Нейтрально"
                                    }
                                    onChange={props.handleChange}
                                    fullWidth
                                    error={Boolean(props.errors.smoking)}
                                    sx={inputSxProps}
                                    select>
                                    <MenuItem value="Нейтрально">Нейтрально</MenuItem>
                                    <MenuItem value="Отрицательно">Отрицательно</MenuItem>
                                    <MenuItem value="Положительно">Положительно</MenuItem>
                                </TextField>
                            </Grid2>
                            <Grid2 size={3}>
                                <TextField
                                    name="drinking"
                                    label="Отношение к алкоголю"
                                    value={props.values.drinking || "Нейтрально"}
                                    onChange={props.handleChange}
                                    fullWidth
                                    error={Boolean(props.errors.drinking)}
                                    sx={inputSxProps}
                                    select>
                                    <MenuItem value="Нейтрально">Нейтрально</MenuItem>
                                    <MenuItem value="Отрицательно">Отрицательно</MenuItem>
                                    <MenuItem value="Положительно">Положительно</MenuItem>
                                </TextField>
                            </Grid2>
                            <Grid2 size={3}>
                                <TextField
                                    name="orientation"
                                    label="Родовая программа"
                                    value={props.values.orientation}
                                    onChange={props.handleChange}
                                    fullWidth
                                    error={Boolean(props.errors.orientation)}
                                    sx={inputSxProps}
                                    select>
                                    <MenuItem value="Социология">Социология</MenuItem>
                                    <MenuItem value="Психология">Психология</MenuItem>
                                    <MenuItem value="Политология">Политология</MenuItem>
                                    <MenuItem value="ГМУ">ГМУ</MenuItem>
                                </TextField>
                            </Grid2>
                            <Grid2 size={3}>
                            <InputLabel color="primary">Дата и время рождения</InputLabel>
                                <DateTimePicker
                                    name="birth_stamp"
                                    value={props.values.birth_stamp ? dayjs.utc(props.values.birth_stamp) : dayjs.utc(Date.now())}
                                    onChange={(value) => {
                                        props.setFieldValue('birth_stamp', value?.utc(false).toISOString());
                                        console.log(value?.toISOString());
                                    }}
                                    disableFuture
                                    timezone="UTC"
                                    sx={{ width: "100%" }}
                                />
                            </Grid2>
                            <Grid2 size={4} alignContent="center">
                                <Button fullWidth variant="contained" type="submit" disabled={props.isSubmitting}>Изменить</Button>
                                {postMsg ? <Typography variant="inherit" color="error" textAlign="center">{postMsg}</Typography> : null}
                                {postFileMsg ? <Typography variant="inherit" color="error" textAlign="center">{postFileMsg}</Typography> : null}
                            </Grid2>
                        </Grid2>
                    </Form>
                // </Paper>
            }
        </Formik>
    )
}

export async function editUserAction(params: PostUserDto): Promise<string | null> {
    return await postUser(params);
}

export async function editUserLoader() {
    const userId = localStorage.getItem("userId");
    if (userId === null) {
        return redirect("/login");
    }

    const user = await getUser(parseInt(userId))

    return user ? user : redirect("/users");
}
