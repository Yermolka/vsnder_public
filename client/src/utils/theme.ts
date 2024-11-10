import { createTheme, ThemeOptions } from '@mui/material/styles';

export const themeOptions: ThemeOptions = createTheme({
  palette: {
    mode: 'light',
    primary: {
      main: '#231942',
      contrastText: '#d01d1d',
    },
    secondary: {
      main: '#e0b1cb',
    },
    background: {
      default: '#231942',
      paper: '#5e548e',
    },
    text: {
      primary: '#e4dfdf',
      secondary: 'rgba(195,184,184,0.6)',
    },
  },
});
