import { useCallback, useEffect } from "react";
import { getLogout } from "../api/auth";
import { useNavigate } from "react-router-dom";

export function Logout() {
    const navigate = useNavigate();

    const logout = useCallback(async () => {
        const res = await getLogout();

        if (res.status === 200) {
            localStorage.clear();
            navigate('/login');
        }
    }, [])

    useEffect(() => {
        logout().catch(console.error);
    }, [logout])
    
    return null;
}
