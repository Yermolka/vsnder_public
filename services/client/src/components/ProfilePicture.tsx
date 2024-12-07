import { Avatar } from "@mui/material";

export interface ProfilePictureProps {
    fileId?: number;
    size?: number;
}

export function ProfilePicture({ fileId, size }: ProfilePictureProps) {
    return (
        <div style={{ display: "flex", height: "100%", width: "100%", alignItems: "center", justifyContent: "center" }}>
            {fileId ? <Avatar src={`/api/file/${fileId}`} sx={{ width: size || 150, height: size || 150 }} /> : <Avatar sx={{ width: size || 150, height: size || 150 }} />}
        </div>
    )
}
