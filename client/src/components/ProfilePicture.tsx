import { Avatar } from "@mui/material";

export interface ProfilePictureProps {
    userId: number;
    hasAvatar: boolean;
    size?: number;
}

export function ProfilePicture({ userId, hasAvatar, size }: ProfilePictureProps) {
    return (
        <div style={{ display: "flex", height: "100%", width: "100%", alignItems: "center", justifyContent: "center" }}>
            {hasAvatar ? <Avatar src={`/api/users/${userId}/file`} sx={{ width: size || 150, height: size || 150 }} /> : <Avatar sx={{ width: size || 150, height: size || 150 }} />}
        </div>
    )
}
