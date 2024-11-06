import { CircularProgress as MUICircularProgress } from "@mui/material";

interface Props {
    size?: number;
    color?: 'error' | 'success' | 'warning' | 'info' | 'inherit' | 'secondary' | 'primary';
    sx?: object;
}

export function CircularProgress({size = 30, color = 'secondary', sx = {} }: Props) {
    return <MUICircularProgress color={color} size={size} sx={{ ...sx }} />
}
