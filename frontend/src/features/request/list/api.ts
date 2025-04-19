import { queryOptions } from "@tanstack/react-query"
import { toast } from "sonner"
import { requestListDTOschema, RequestModel, fromRequestDTO } from "./model"
import { typedQuery } from "@shared/lib/precooked-methods"
import { instance } from "@shared/api"

export const api = {
    baseKey: ["application"],
    baseUrl: "v1/marketplace/applications/",

    getAllRequests: () =>
        queryOptions<RequestModel[]>({
            queryKey: [...api.baseKey],
            queryFn: () =>
                typedQuery({
                    request: instance.get(api.baseUrl),
                    dtoSchema: requestListDTOschema,
                    fromDTO: (dtoList: any[]) => dtoList.map(fromRequestDTO),
                }).catch((err) => {
                    console.error(err)
                    toast.error("Не удалось загрузить список заявок")

                    throw err
                }),
        }),
}
