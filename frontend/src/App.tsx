import { CssBaseline, Container } from '@mui/material';
import { ThemeProvider, createTheme } from '@mui/material/styles';
import { useRoutes } from 'react-router-dom';
import routes from './routes';

const theme = createTheme({
  palette: {
    mode: 'light',
    primary: { main: '#2953A4' },
    secondary: { main: '#FFC433' },
  },
});

export default function App() {
  const element = useRoutes(routes);
  return (
    <ThemeProvider theme={theme}>
      <CssBaseline />
      <Container maxWidth="lg">{element}</Container>
    </ThemeProvider>
  );
}
