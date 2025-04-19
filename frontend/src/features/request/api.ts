import { queryOptions } from "@tanstack/react-query"
import {
    requestListDTOschema,
    RequestModel,
    fromRequestDTO,
    requestDTOschema,
} from "@features/request/model"
import { typedQuery } from "@shared/lib/precooked-methods"
import { AxiosResponse } from "axios"
import { instance } from "@shared/api"
import { toast } from "sonner"

export const api = {
    baseKey: "request",
    baseUrl: "request",

    getAllRequests: () =>
        queryOptions<RequestModel[]>({
            queryKey: [...api.baseKey],
            queryFn: () => {
                const req: Promise<AxiosResponse> = instance.get(
                    api.baseUrl
                )

                return typedQuery({
                    request: req,
                    dtoSchema: requestListDTOschema,
                    fromDTO: (dtoList: any[]) => dtoList.map(fromRequestDTO),
                }).catch((err) => {
                    console.error(err)
                    toast.error("Не удалось загрузить список заявок")
                    throw err
                })
            },
        }),

    getRequestById: (id: string | null) =>
        queryOptions<RequestModel>({
            queryKey: [...api.baseKey, "ById", id],
            queryFn: () => {
                if (id === null) {
                    return Promise.reject(new Error("ID заявки не указан"))
                }

                const req: Promise<AxiosResponse> = instance.get(
                    `${api.baseUrl}/${id}`
                )

                return typedQuery({
                    request: req,
                    dtoSchema: requestDTOschema,
                    fromDTO: fromRequestDTO,
                }).catch((err) => {
                    console.error(err)
                    toast.error(`Не удалось загрузить заявку (id: ${id})`)
                    throw err
                })
            },
        }),
}
