import { redirect, useLoaderData, useNavigate } from "react-router-dom";
import { getUser, postUser, postUserImage } from "../api/user";
import { Formik, Form } from "formik";
import { editUserValidationSchema } from "../utils/validation";
import { Button, Grid2, Input, MenuItem, Paper, Select, TextField } from "@mui/material";
import { GetUserDto, PostUserDto, postUserFromGetUserDto } from "../dto/user";
import { Form as ReactForm } from "react-router-dom";
import { ChangeEvent, useState } from "react";

export default function EditUser() {
    const loaderData = useLoaderData() as GetUserDto;
    const user = postUserFromGetUserDto(loaderData);
    const navigate = useNavigate();
    const [file, setFile] = useState<File | null>(null);

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
                editUserAction(values)
                    .then(() => {
                        navigate("/users");
                    })
                    .catch((err) => {
                        console.error(err);
                        navigate("/users");
                    });
                setSubmitting(false);
            }}>
            {props =>
                <Paper elevation={3} style={{ padding: "25px", margin: "10px" }}>
                    <ReactForm onSubmit={(event) => {
                        postUserImage(loaderData.id, file).then(value => console.log(value));
                        event.preventDefault();
                    }}>
                        <Grid2 container direction="row" alignItems="stretch" justifyItems="center" spacing={2} columns={2}>
                            <Grid2 size={1}>
                                <Input type="file" name="img" id="img" onChange={handleFileChange} />
                            </Grid2>
                            <Grid2 size={1}>
                                <Button variant="contained" type="submit" >Загрузить аватарку</Button>
                            </Grid2>
                        </Grid2>
                    </ReactForm>
                    <Form className="edit-user-form">
                        <Grid2 container spacing={2} columns={{ md: 6, xs: 3 }} alignItems="stretch" justifyContent="center">
                            <Grid2 size={3}>
                                <TextField
                                    type="number"
                                    name="age"
                                    label="Возраст"
                                    value={props.values.age}
                                    onChange={props.handleChange}
                                    fullWidth />
                            </Grid2>
                            <Grid2 size={3}>
                                <Select
                                    label="Программа"
                                    name="orientation"
                                    value={props.values.orientation}
                                    onChange={props.handleChange}
                                    fullWidth>
                                    <MenuItem value="Социология">Социология</MenuItem>
                                    <MenuItem value="Психология">Психология</MenuItem>
                                    <MenuItem value="Политология">Политология</MenuItem>
                                    <MenuItem value="ГМУ">ГМУ</MenuItem>
                                </Select>
                            </Grid2>
                            <Grid2 size={3}>
                                <Select
                                    label="Курс"
                                    name="year_of_study"
                                    value={props.values.year_of_study}
                                    onChange={props.handleChange}
                                    fullWidth>
                                    <MenuItem value={1}>1</MenuItem>
                                    <MenuItem value={2}>2</MenuItem>
                                    <MenuItem value={3}>3</MenuItem>
                                    <MenuItem value={4}>4</MenuItem>
                                </Select>
                            </Grid2>
                            <Grid2 size={3}>
                                <TextField
                                    type="text"
                                    name="interests"
                                    label="Увлечения"
                                    value={props.values.interests}
                                    onChange={props.handleChange}
                                    fullWidth />
                            </Grid2>
                            <Grid2 size={3}>
                                <TextField
                                    type="text"
                                    name="vsnInterests"
                                    label="Увлечения на ВСН"
                                    value={props.values.vsn_interests}
                                    onChange={props.handleChange}
                                    fullWidth />
                            </Grid2>
                            <Grid2 size={3}>
                                <TextField
                                    type="text"
                                    name="placesToVisit"
                                    label="Места, которые ты хочешь посетить"
                                    value={props.values.places_to_visit}
                                    onChange={props.handleChange}
                                    fullWidth />
                            </Grid2>
                            <Grid2 size={3}>
                                <TextField
                                    type="text"
                                    name="studyPlaces"
                                    label="Где ты ботаешь"
                                    value={props.values.study_places}
                                    onChange={props.handleChange}
                                    fullWidth />
                            </Grid2>
                            <Grid2 size={3}>
                                <TextField
                                    type="text"
                                    name="music"
                                    label="Любимая музыка"
                                    value={props.values.music}
                                    onChange={props.handleChange}
                                    fullWidth />
                            </Grid2>
                            <Grid2 size={3}>
                                <TextField
                                    type="text"
                                    name="favoriteMovies"
                                    label="Любимые фильмы"
                                    value={props.values.favorite_movies}
                                    onChange={props.handleChange}
                                    fullWidth />
                            </Grid2>
                            <Grid2 size={3}>
                                <TextField
                                    type="text"
                                    name="religion"
                                    label="Религия"
                                    value={props.values.religion}
                                    onChange={props.handleChange}
                                    fullWidth />
                            </Grid2>
                            <Grid2 size={3}>
                                <TextField
                                    type="text"
                                    name="status"
                                    label="Статус?"
                                    value={props.values.status}
                                    onChange={props.handleChange}
                                    fullWidth />
                            </Grid2>
                            <Grid2 size={3}>
                                <TextField
                                    type="text"
                                    name="futurePlans"
                                    label="Планы на будущее"
                                    value={props.values.future_plans}
                                    onChange={props.handleChange}
                                    fullWidth />
                            </Grid2>
                            <Grid2 size={3}>
                                <TextField
                                    type="text"
                                    name="familyOpinion"
                                    label="Отношение к семье"
                                    value={props.values.family_opinion}
                                    onChange={props.handleChange}
                                    fullWidth />
                            </Grid2>
                            <Grid2 size={3}>
                                <TextField
                                    type="text"
                                    name="favoriteProgrammingLanguage"
                                    label="Любимый язык программирования"
                                    value={props.values.favorite_programming_language}
                                    onChange={props.handleChange}
                                    fullWidth />
                            </Grid2>
                            <Grid2 size={3}>
                                <Select
                                    label="Отношение к курению"
                                    name="smoking"
                                    value={props.values.smoking}
                                    onChange={props.handleChange}
                                    fullWidth>
                                    <MenuItem value="Нейтрально">Нейтрально</MenuItem>
                                    <MenuItem value="Отрицательно">Отрицательно</MenuItem>
                                    <MenuItem value="Положительно">Положительно</MenuItem>
                                </Select>
                            </Grid2>
                            <Grid2 size={3}>
                                <Select
                                    label="Отношение к алкоголю"
                                    name="drinking"
                                    value={props.values.drinking}
                                    onChange={props.handleChange}
                                    fullWidth>
                                    <MenuItem value="Нейтрально">Нейтрально</MenuItem>
                                    <MenuItem value="Отрицательно">Отрицательно</MenuItem>
                                    <MenuItem value="Положительно">Положительно</MenuItem>
                                </Select>
                            </Grid2>
                            <Grid2 size={3}>
                                <TextField
                                    type="text"
                                    name="top3People"
                                    label="Топ 3 персоны"
                                    value={props.values.top_3_people}
                                    onChange={props.handleChange}
                                    fullWidth />
                            </Grid2>
                            <Grid2 size={4} alignContent="center">
                                <Button fullWidth variant="contained" type="submit" disabled={props.isSubmitting}>Изменить</Button>
                            </Grid2>
                        </Grid2>
                    </Form>
                </Paper>
            }
        </Formik>
    )
}

export async function editUserAction(params: PostUserDto) {
    const res = await postUser(params);

    return redirect("/users");
}

export async function editUserLoader() {
    const userId = localStorage.getItem("userId");
    if (userId === null) {
        return redirect("/login");
    }

    const user = await getUser(parseInt(userId))

    return user ? user : redirect("/users");
}
