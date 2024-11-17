import * as yup from 'yup';

export const changePasswordValidationSchema = yup.object().shape({
    old_password: yup.string().required("Это обязательное поле"),
    new_password: yup.string().min(6, "Пароль должен содержать не менее 6 символов").required("Это обязательное поле"),
    new_password_re: yup.string().required("Это обязательное поле").test("passwords-match", "Пароли не совпадают", function(value){return value === this.parent.new_password}),
})

export const editUserValidationSchema = yup.object().shape({
    age: yup.number().min(0),
    orientation: yup.string().max(128),
    year_of_study: yup.number().min(1).max(4),
    interests: yup.string().max(128),
    vsnInterests: yup.string().max(128),
    places_to_visit: yup.string().max(128),
    study_places: yup.string().max(128),
    music: yup.string().max(128),
    favorite_movies: yup.string().max(128),
    religion: yup.string().max(128),
    status: yup.string().max(128),
    future_plans: yup.string().max(128),
    family_opinion: yup.string().max(128),
    favorite_programming_language: yup.string().max(128),
    smoking: yup.string().max(128),
    top_3_people: yup.string().max(128),
    drinking: yup.string().max(128),
    birth_stamp: yup.string(),
    birth_city: yup.string().max(128),
})
