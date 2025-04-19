import { queryOptions } from "@tanstack/react-query"
import {
    fromMentorArrayDTO,
    mentorApi,
    mentorDTOschema,
} from "@entities/mentor"
import { typedQuery } from "@shared/lib/precooked-methods"
import { instance } from "@shared/api"

export const getMentorById = ({ mentorId }: { mentorId: number }) =>
    queryOptions({
        queryKey: [...mentorApi.baseUrl, "ById"],
        queryFn: () =>
            typedQuery({
                request: instance.get(`${mentorApi.baseUrl}/${mentorId}`),
                dtoSchema: mentorDTOschema.array(),
                fromDTO: fromMentorArrayDTO,
            }),
    })
