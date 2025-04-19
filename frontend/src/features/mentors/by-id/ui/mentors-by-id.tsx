import { useQuery } from "@tanstack/react-query"
import { getMentorById } from "../api"
import { MentorId } from "@entities/mentor"

export function MentorById({ username }: MentorId) {
    const { data, isLoading } = useQuery(getMentorById({ username }))

    if (isLoading) {
        return <div>Загрузка...</div>
    }

    if (!data) {
        return <div>Что-то пошло не так</div>
    }

    return <div>{data.fullName}</div>
}
