import { Avatar } from "@mui/material";
import { getHasUserProfilePicture } from "../api/user";
import { useEffect, useState } from "react";

export interface ProfilePictureProps {
    userId: number;
}

export function ProfilePicture({ userId }: ProfilePictureProps) {
    const [img, setImg] = useState<string | null>(null);
    
    const fetchImg = async () => {
        const res = await getHasUserProfilePicture(userId);
        if (res) {
            setImg(`/api/users/${userId}/file`);
        }
    };

    useEffect(() => {
        fetchImg();
    }, []);

    return (
        <>
            {img ? <img src={img} width={64} height={64} /> : <Avatar sx={{ width: 64, height: 64}} />}
        </>
    )
}
