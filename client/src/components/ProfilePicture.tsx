import { Avatar } from "@mui/material";
import { getUserProfilePicture } from "../api/user";
import { useEffect, useState } from "react";

export interface ProfilePictureProps {
    userId: number;
}

export function ProfilePicture({ userId }: ProfilePictureProps) {
    const [img, setImg] = useState<string | null>(null);

    const fetchImg = async () => {
        const res = await getUserProfilePicture(userId);
        if (res !== null) {
            setImg(res);
        }
    };

    useEffect(() => {
        fetchImg();
    }, []);

    return (
        <>
            {img ? <img src={img} /> : <Avatar />}
        </>
    )
}
