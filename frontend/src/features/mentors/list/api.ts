import { queryOptions } from "@tanstack/react-query"
import { toast } from "sonner"
import {
    fromMentorArrayDTO,
    mentorApi,
    mentorDTOschema,
    // mockMentorsDTO,
} from "@entities/mentor"
import { typedQuery } from "@shared/lib/precooked-methods"
import { instance } from "@shared/api"

export const getMentorsList = (queryParams?: Record<string, any>) =>
    queryOptions({
        queryKey: [...mentorApi.baseKey, "list", queryParams],
        queryFn: () =>
            typedQuery({
                request: instance.get(`${mentorApi.baseUrl}`, {
                    params: queryParams,
                }),
                // request: Promise.resolve({
                //     data: mockMentorsDTO,
                //     status: 200,
                //     statusText: "OK",
                //     headers: {},
                //     config: {
                //         headers: {}, // Added required headers property
                //     },
                // }) as Promise<AxiosResponse>,
                dtoSchema: mentorDTOschema.array(),
                fromDTO: fromMentorArrayDTO,
            }).catch((err) => {
                console.error(err)
                toast.error("something went wrong in mentors list")
            }),
    })
