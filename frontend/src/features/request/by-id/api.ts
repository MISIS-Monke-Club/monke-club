import { toast } from "sonner"
import { queryOptions } from "@tanstack/react-query"
import {
    fullRequestDTOschema,
    FullRequestModel,
    fromFullRequestDTO,
} from "./model"
import { instance } from "@shared/api"
import { typedQuery } from "@shared/lib/precooked-methods"

export const api = {
    baseKey: ["application"],
    baseUrl: "/marketplace/applications/",

    getRequestBySlug: (slug: string) =>
        queryOptions<FullRequestModel>({
            queryKey: [...api.baseKey, slug],
            queryFn: () =>
                typedQuery({
                    request: instance.get(`${api.baseUrl}${slug}/`),
                    dtoSchema: fullRequestDTOschema,
                    fromDTO: fromFullRequestDTO,
                }).catch((err) => {
                    console.error(err)
                    toast.error("Не удалось загрузить заявку")
                    throw err
                }),
        }),
}
