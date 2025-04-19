import { z } from "zod"

export const mentorDTOschema = z.object({
    username: z.string(),
    full_name: z.string(),
    services: z.array(
        z.object({
            id: z.number(),
            name: z.string(),
        })
    ),
    subjects: z.array(
        z.object({
            id: z.number(),
            name: z.string(),
        })
    ),
    count_successful_transactions: z.number(),
    photo: z.string().url(),
    rating: z.number(),
})

export type MentorModel = {
    username: string
    fullName: string
    services: { id: number; name: string }[]
    subjects: { id: number; name: string }[]
    countSuccessfulTransactions: number
    photo: string
    rating: number
}
