import { FormEvent, useCallback } from "react"
import { toast } from "sonner"
import { useDispatch } from "react-redux"
import { useNavigate } from "react-router-dom"
import classes from "./login.module.scss"
import { useLogin } from "@features/auth"
import { Button } from "@shared/ui/button"
import { setUserId } from "@entities/session"
import { Input } from "@shared/ui/input"

export function LoginPage() {
    const { isMutationPending } = useLogin()
    const dispatch = useDispatch()
    const navigate = useNavigate()

    const handleSubmit = useCallback(
        (e: FormEvent<HTMLFormElement>) => {
            e.preventDefault()

            dispatch(setUserId({ userId: "1" }))
            navigate("/")
        },
        [dispatch, navigate]
    )

    const handleRegister = () => {
        toast.success("Вы зарегистрировались")
    }

    return (
        <form onSubmit={handleSubmit} className={classes.form}>
            <Input name='login' placeholder='Введите ваш логин' required />
            <Input name='password' placeholder='Введите ваш логин' required />
            <div className={classes.actions}>
                <Button type='submit' disabled={isMutationPending}>
                    Логин
                </Button>
                <Button
                    type='submit'
                    disabled={isMutationPending}
                    onClick={handleRegister}
                >
                    Зарегистрироваться
                </Button>
            </div>
        </form>
    )
}
