import { Paper, Typography } from "@mui/material";
import { FallbackProps } from "react-error-boundary";

const ErrorFallback = (props: FallbackProps) => (
    <Paper elevation={3}>
        <Typography>{props.error.toString()}</Typography>
    </Paper>
)

export default ErrorFallback;
