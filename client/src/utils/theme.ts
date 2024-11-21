import { createTheme, ThemeOptions } from '@mui/material/styles';

export const themeOptions: ThemeOptions = createTheme({
  palette: {
    mode: 'light',
    primary: {
      main: '#2f2f2f',
      contrastText: '#ffffff',
    },
    secondary: {
      main: '#ffffff',
      contrastText: '#ffffff',
    },
    background: {
      default: '#2f2f2f',
      paper: '#2f2f2f',
    },
    text: {
      primary: '#ffffff',
      secondary: '#ffffff',
      disabled: '#ffffff',
    },
    error: {
        main: '#E57373',
    },
    info: {
        main: '#ffffff',
    }
  },
});
