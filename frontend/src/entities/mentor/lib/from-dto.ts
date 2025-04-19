import { z } from "zod"
import { mentorDTOschema, MentorModel } from "../model"

export const fromMentorDTO = (
    mentor: z.infer<typeof mentorDTOschema>
): MentorModel => ({
    username: mentor.username,
    fullName: mentor.full_name,
    photo: mentor.photo,
    rating: mentor.rating,
    services: mentor.services,
    subjects: mentor.subjects,
    countSuccessfulTransactions: mentor.count_successful_transactions,
})

export const fromMentorArrayDTO = (
    mentors: z.infer<ReturnType<typeof mentorDTOschema.array>>
): MentorModel[] => mentors.map((el) => fromMentorDTO(el))
