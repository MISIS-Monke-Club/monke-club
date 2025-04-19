import { FormEvent, useCallback } from "react"
import { z } from "zod"
import { toast } from "sonner"
import classes from "./login.module.scss"
import { useLogin } from "@features/auth"
import { Button } from "@shared/ui/button/ui"
import { Input } from "@shared/ui/input"

const loginPageParamsSchema = z.object({
    login: z.string().min(1),
    password: z.string().min(1),
})

export function LoginPage() {
    const { isMutationPending, login } = useLogin()

    const handleSubmit = useCallback(
        (e: FormEvent<HTMLFormElement>) => {
            e.preventDefault()

            const formData = new FormData(e.currentTarget)
            const parsedData = loginPageParamsSchema.safeParse(
                Object.fromEntries(formData)
            )
            const { data, error, success } = parsedData

            if (success) {
                login({
                    login: data.login,
                    password: data.password,
                })
            } else {
                toast.error("Ошибка ввода")
                console.error(error)
            }
        },
        [login]
    )

    return (
        <form onSubmit={handleSubmit} className={classes.form}>
            <Input name='login' placeholder='Введите ваш логин' required />
            <Input name='password' placeholder='Введите ваш логин' required />
            <div className={classes.actions}>
                <Button type='submit' disabled={isMutationPending}>
                    Логин
                </Button>
                <Button type='submit' disabled={isMutationPending}>
                    Зарегистрироваться
                </Button>
            </div>
        </form>
    )
}
