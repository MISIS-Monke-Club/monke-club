import { z } from "zod"

export const mentorPageDTOschema = z.object({
    username: z.string(),
    full_name: z.string(),
    description: z.string().optional(),
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
    photo: z.string().url().nullable(),
    rating: z.number(),
    social_network: z.array(
        z.object({
            name: z.string(),
            text: z.string(),
        })
    ),
    course: z.number(),
    faculty: z.string(),
})

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
    rating: z.number(),
    photo: z.string().url().nullable(),
    count_successful_transactions: z.number(),
})

export type MentorModel = {
    username: string
    fullName: string
    services: { id: number; name: string }[]
    subjects: { id: number; name: string }[]
    rating: number
    photo: string | null
    countSuccessfulTransactions: number
}

export type MentorPageModel = {
    username: string
    fullName: string
    description?: string
    services: { id: number; name: string }[]
    subjects: { id: number; name: string }[]
    countSuccessfulTransactions: number
    photo: string | null
    rating: number
    socialNetwork: { name: string; text: string }[]
    course: number
    faculty: string
}

export type MentorId = Pick<MentorModel, "username">
