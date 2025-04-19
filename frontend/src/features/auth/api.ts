import { MutationOptions } from "@tanstack/react-query"
import { userApi, userDTOschema, UserModel } from "@entities/user"
import { client, instance } from "@shared/api"
import { typedQuery } from "@shared/lib/precooked-methods"
import { fromUserDTO } from "@entities/user"

export type LoginParamsModel = {
    login: UserModel["login"]
    password: UserModel["login"]
}

export const api = {
    ...userApi,
    login: (): MutationOptions<UserModel, unknown, LoginParamsModel> => ({
        mutationFn: (params) =>
            typedQuery({
                request: instance.post(`${userApi.baseUrl}/login`, {
                    ...params,
                }),
                dtoSchema: userDTOschema,
                fromDTO: fromUserDTO,
            }),
        onSuccess: () => {
            client.invalidateQueries({
                queryKey: [...api.baseKey],
            })
        },
    }),
}
