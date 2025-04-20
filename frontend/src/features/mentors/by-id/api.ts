import { queryOptions } from "@tanstack/react-query"
import { toast } from "sonner"
import {
    fromMentorPageDTO,
    mentorApi,
    mentorPageDTOschema,
} from "@entities/mentor"
import { typedQuery } from "@shared/lib/precooked-methods"
import { instance } from "@shared/api"
import { MentorId } from "@entities/mentor"

export const getMentorById = ({ username }: MentorId) =>
    queryOptions({
        queryKey: [...mentorApi.baseUrl, "ById"],
        queryFn: () =>
            typedQuery({
                request: instance.get(`${mentorApi.baseUrl}/${username}`),
                dtoSchema: mentorPageDTOschema,
                fromDTO: fromMentorPageDTO,
            }).catch((err) => {
                console.error(err)
                toast.error("Cant display this mentor")
            }),
    })
