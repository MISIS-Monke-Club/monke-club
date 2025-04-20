import { z } from "zod"
import {
    mentorDTOschema,
    MentorModel,
    mentorPageDTOschema,
    MentorPageModel,
} from "../model/domain"

export const fromMentorPageDTO = (
    mentor: z.infer<typeof mentorPageDTOschema>
): MentorPageModel => ({
    username: mentor.username,
    course: mentor.course,
    faculty: mentor.faculty,
    socialNetwork: mentor.social_network,
    description: mentor.description,
    fullName: mentor.full_name,
    photo: mentor.photo,
    rating: mentor.rating,
    services: mentor.services,
    subjects: mentor.subjects,
    countSuccessfulTransactions: mentor.count_successful_transactions,
})

export const fromMentorDTO = (
    mentor: z.infer<typeof mentorDTOschema>
): MentorModel => ({
    username: mentor.username,
    fullName: mentor.full_name,
    photo: mentor.photo,
    rating: mentor.rating,
    countSuccessfulTransactions: mentor.count_successful_transactions,
    services: mentor.services,
    subjects: mentor.subjects,
})

export const fromMentorArrayDTO = (
    mentors: z.infer<ReturnType<typeof mentorDTOschema.array>>
): MentorModel[] => mentors.map((el) => fromMentorDTO(el))
