import { Avatar } from "@mui/material";

export interface ProfilePictureProps {
    userId: number;
    hasAvatar: boolean;
}

export function ProfilePicture({ userId, hasAvatar }: ProfilePictureProps) {
    return (
        <>
            {hasAvatar ? <img src={`/api/users/${userId}/file`} width={64} height={64} /> : <Avatar sx={{ width: 64, height: 64}} />}
        </>
    )
}
