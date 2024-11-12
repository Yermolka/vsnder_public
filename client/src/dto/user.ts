export interface PostUserDto {
    age?: number;
    orientation?: string;
    interests?: string;
    vsn_interests?: string;
    places_to_visit?: string;
    study_places?: string;
    music?: string;
    favorite_movies?: string;
    religion?: string;
    status?: string;
    future_plans?: string;
    family_opinion?: string;
    favorite_programming_language?: string;
    lizards_or_russians?: Boolean;
    smoking?: string;
    top_3_people?: string;
    drinking?: string;
}

export interface GetShortUserDto {
    id: number;
    first_name: string;
    last_name: string;
    orientation?: string;
    year_of_study: number;
}

export function postUserFromGetUserDto(user: GetUserDto): PostUserDto {
    return {
        age: user.age || 0,
        orientation: user.orientation || '',
        interests: user.interests || '',
        vsn_interests: user.vsn_interests || '',
        places_to_visit: user.places_to_visit || '',
        study_places: user.study_places || '',
        music: user.music || '',
        favorite_movies: user.favorite_movies || '',
        religion: user.religion || '',
        status: user.status || '',
        future_plans: user.future_plans || '',
        family_opinion: user.family_opinion || '',
        favorite_programming_language: user.favorite_programming_language || '',
        lizards_or_russians: user.lizards_or_russians || false,
        smoking: user.smoking || '',
        top_3_people: user.top_3_people || '',
        drinking: user.drinking || '',
    }
}

export interface UserAuthDto {
    username: string;
    password: string;
}

export interface UserChangePasswordDto {
    old_password: string;
    new_password: string;
}

export interface GetUserDto {
    id: number;
    first_name: string;
    last_name: string;
    age?: number;
    orientation?: string;
    year_of_study: number;
    interests?: string;
    vsn_interests?: string;
    places_to_visit?: string;
    study_places?: string;
    music?: string;
    favorite_movies?: string;
    religion?: string;
    status?: string;
    future_plans?: string;
    family_opinion?: string;
    favorite_programming_language?: string;
    lizards_or_russians?: Boolean;
    smoking?: string;
    top_3_people?: string;
    drinking?: string;
}
