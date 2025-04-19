import { queryOptions } from "@tanstack/react-query"
import {
    fromMentorArrayDTO,
    mentorApi,
    mentorDTOschema,
} from "@entities/mentor"
import { typedQuery } from "@shared/lib/precooked-methods"
import { instance } from "@shared/api"

export const getMentorsList = queryOptions({
    queryKey: [...mentorApi.baseUrl, "list"],
    queryFn: () =>
        typedQuery({
            request: instance.get(`${mentorApi.baseUrl}`),
            dtoSchema: mentorDTOschema.array(),
            fromDTO: fromMentorArrayDTO,
        }),
})
