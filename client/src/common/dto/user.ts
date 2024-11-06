export interface GetUserDto {
    id: number;
    username: string;
    first_name: string;
    last_name: string;
    age: number | null;
}

export interface PostUserDto {
    username: string;
    password: string;
}
