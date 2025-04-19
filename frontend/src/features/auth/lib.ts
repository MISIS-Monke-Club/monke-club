import { useMutation } from "@tanstack/react-query"
import { toast } from "sonner"
import { useDispatch } from "react-redux"
import { LoginParamsModel } from "./api"
import { authApi } from "."
import { setUserId } from "@entities/session"

export const useLogin = () => {
    const { mutateAsync, isPending, isError } = useMutation(authApi.login())
    const dispatch = useDispatch()

    const mutation = (params: LoginParamsModel) =>
        mutateAsync({ ...params })
            .then((res) => {
                if (res) {
                    dispatch(setUserId({ userId: res.id }))
                } else {
                    toast.error("cant add user to the redux")
                }
            })
            .catch((err) => {
                console.error(err)
                toast.error("cant login you right now")
            })

    return {
        login: mutation,
        isMutationPending: isPending,
        isMutationError: isError,
    }
}
