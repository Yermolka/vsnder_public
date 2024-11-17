import { createTheme, ThemeOptions } from '@mui/material/styles';

export const themeOptions: ThemeOptions = createTheme({
  palette: {
    mode: 'light',
    primary: {
      main: '#9c27b0',
      contrastText: '#e1bee7',
    },
    secondary: {
      main: '#ffffff',
    },
    background: {
      default: '#4A148C',
      paper: '#6A1B9A',
    },
    text: {
      primary: '#e4dfdf',
      secondary: 'rgba(195,184,184,0.6)',
    },
    error: {
        main: '#E57373',
    }
  },
});
