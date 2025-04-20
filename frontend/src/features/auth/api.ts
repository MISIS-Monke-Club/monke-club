import { MutationOptions } from "@tanstack/react-query"
import { userApi, UserModel } from "@entities/user"
import { client, instance } from "@shared/api"

export type LoginParamsModel = {
    username: UserModel["login"]
    password: UserModel["login"]
}

export const api = {
    ...userApi,
    login: (): MutationOptions<UserModel, unknown, LoginParamsModel> => ({
        mutationFn: (params) =>
            instance.post(`${userApi.baseUrl}/login/`, params),
        onSuccess: () => {
            client.invalidateQueries({
                queryKey: [...api.baseKey],
            })
        },
    }),
}
