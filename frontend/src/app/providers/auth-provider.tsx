import { useSelector } from "react-redux"
import { Navigate, Outlet } from "react-router-dom"
import { selectUserId } from "@entities/session"

export function AuthProvider() {
    const userId = useSelector(selectUserId)

    if (!userId) {
        return <Navigate to='/login' />
    }

    return <Outlet />
}
