import { queryOptions } from "@tanstack/react-query"
import { fromMentorDTO, mentorApi, mentorDTOschema } from "@entities/mentor"
import { typedQuery } from "@shared/lib/precooked-methods"
import { instance } from "@shared/api"
import { MentorId } from "@entities/mentor"

export const getMentorById = ({ username }: MentorId) =>
    queryOptions({
        queryKey: [...mentorApi.baseUrl, "ById"],
        queryFn: () =>
            typedQuery({
                request: instance.get(`${mentorApi.baseUrl}/${username}`),
                dtoSchema: mentorDTOschema,
                fromDTO: fromMentorDTO,
            }),
    })
