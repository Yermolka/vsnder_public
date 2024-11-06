import { PropsWithChildren, useMemo } from "react";

import { createTheme, CssBaseline, ThemeProvider } from "@mui/material";

import { PRIMARY_COLOR, SECONDARY_COLOR } from "../../../../common/consts/common";
import { useAppSelector } from "../../../../common/redux/hooks";

export function AppThemeProvider({ children }: PropsWithChildren) {
    const theme = useMemo(
        () => 
            createTheme({
                palette: {
                    mode: "dark",
                    primary: {
                        main: PRIMARY_COLOR,
                    },
                    secondary: {
                        main: SECONDARY_COLOR,
                    },
                    text: {
                        primary: '#000',
                        secondary: '#050505'
                    }
                },
            }), []
    );

    return (
        <ThemeProvider theme={theme}>
            <CssBaseline />
            {children}
        </ThemeProvider>
    )
}
