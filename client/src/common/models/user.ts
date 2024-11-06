import { GetUserDto } from "../dto/user";

export interface User {
    id: number;
    username: string;
    firstName: string;
    lastName: string;
    age: number | null;
}

export function createUserFromDto(dto: GetUserDto): User {
    return {
        id: dto.id,
        username: dto.username,
        firstName: dto.first_name,
        lastName: dto.last_name,
        age: dto.age ?? null,
    }
}
