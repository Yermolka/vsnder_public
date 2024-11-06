import { useState } from "react";

import VisibilityIcon from '@mui/icons-material/Visibility';
import VisibilityOffIcon from '@mui/icons-material/VisibilityOff';
import { IconButton, Input, InputAdornment, TextField, TextFieldProps } from "@mui/material";

export function PasswordField(props: TextFieldProps) {
    const [showPassword, setShowPassword] = useState(false);

    const handleTogglePasswordVisibility = () => {
        setShowPassword(prevShowPassword => !prevShowPassword);
    };

    return (
        <TextField
          InputProps={{
            endAdornment: (
                <InputAdornment position="end">
                    <IconButton onClick={handleTogglePasswordVisibility} tabIndex={-1}>
                        {showPassword ? <VisibilityOffIcon /> : <VisibilityIcon />}
                    </IconButton>
                </InputAdornment>
            ),
          }}
          type={showPassword ? 'text' : 'password'}
          {...props} 
        />
    );
}
