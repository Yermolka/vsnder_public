import { useCallback, useEffect } from "react";
import { getLogout } from "../api/auth";
import { useNavigate } from "react-router-dom";

export function Logout() {
    const navigate = useNavigate();
    const logout = useCallback(async () => {
        const res = await getLogout();

        if (res.status === 200 || res.status === 401) {
            localStorage.clear();
            navigate('/login');
        }
    }, [])

    useEffect(() => {
        logout().catch(err => {
            localStorage.clear();
            navigate("/login");
        }).finally(() => {
            localStorage.clear();
            navigate("/login");
        });
    }, [logout])

    return null;
}
