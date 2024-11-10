import * as yup from 'yup';

export const changePasswordValidationSchema = yup.object().shape({
    old_password: yup.string().required("Это обязательное поле"),
    new_password: yup.string().min(6, "Пароль должен содержать не менее 6 символов").required("Это обязательное поле"),
    new_password_re: yup.string().required("Это обязательное поле").test("passwords-match", "Пароли не совпадают", function(value){return value === this.parent.new_password}),
})

export const editUserValidationSchema = yup.object().shape({
    age: yup.number().min(0),
    orientation: yup.string().max(128),
    interests: yup.string().max(128),
    vsnInterests: yup.string().max(128),
    placesToVisit: yup.string().max(128),
    studyPlaces: yup.string().max(128),
    music: yup.string().max(128),
    favoriteMovies: yup.string().max(128),
    religion: yup.string().max(128),
    status: yup.string().max(128),
    futurePlans: yup.string().max(128),
    familyOpinion: yup.string().max(128),
    favoriteProgrammingLanguage: yup.string().max(128),
    smoking: yup.string().max(128),
    top3People: yup.string().max(128),
    drinking: yup.string().max(128),
})
