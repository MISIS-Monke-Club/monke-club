import { useMemo } from "react"
import { useParams } from "react-router-dom"
import { z } from "zod"
import { MentorById } from "@features/mentors/by-id"

const mentorsPageParamsSchema = z.object({
    mentorId: z
        .string()
        .min(1, "что-то пошло не так, вы ввели неправильную ссылку"),
})

export function MentorPage() {
    const params = useParams()

    const id: string | null = useMemo(() => {
        const parsedParams = mentorsPageParamsSchema.safeParse(params)

        if (parsedParams.success) {
            return parsedParams.data.mentorId
        }

        return null
    }, [params])

    if (!id) {
        throw new Error("Cant handle this url, wrong params")
    }

    return (
        <div>
            <h1>Mentor`s page</h1>
            <MentorById username={id} />
        </div>
    )
}
