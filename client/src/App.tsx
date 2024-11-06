import { useNavigate, useMatch, Outlet } from 'react-router-dom';

import './App.css';
import { useEffect } from 'react';

export function App() {
    const navigate = useNavigate();
    const appMatch = useMatch({path: '/', end: true });

    useEffect(() => {
        if (appMatch) {
            return navigate('/login');
        }
    }, [appMatch]);

  return (
    <Outlet />
  );
}
