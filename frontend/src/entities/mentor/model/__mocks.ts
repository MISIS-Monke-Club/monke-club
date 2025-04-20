import { z } from "zod"
import {
    mentorDTOschema,
    MentorModel,
    mentorPageDTOschema,
    MentorPageModel,
} from "./domain"

export const mockMentorPageDTO: z.infer<typeof mentorPageDTOschema> = {
    username: "Topand",
    full_name: "Александр Топанд",
    description: "Опытный ментор по математике и программированию.",
    services: [
        { id: 1, name: "Репетиторство" },
        { id: 2, name: "Подготовка к ЕГЭ" },
    ],
    subjects: [
        { id: 1, name: "Математика" },
        { id: 2, name: "Информатика" },
    ],
    count_successful_transactions: 12,
    photo: null,
    rating: 4.9,
    social_network: [
        { name: "tg", text: "alex_topand" },
        { name: "vk", text: "topand_vk" },
    ],
    course: 3,
    faculty: "Факультет прикладной математики",
}

export const mockMentorPageModel: MentorPageModel = {
    username: "Topand",
    fullName: "Александр Топанд",
    description: "Опытный ментор по математике и программированию.",
    services: [
        { id: 1, name: "Репетиторство" },
        { id: 2, name: "Подготовка к ЕГЭ" },
    ],
    subjects: [
        { id: 1, name: "Математика" },
        { id: 2, name: "Информатика" },
    ],
    countSuccessfulTransactions: 12,
    photo: null,
    rating: 4.9,
    socialNetwork: [
        { name: "tg", text: "alex_topand" },
        { name: "vk", text: "topand_vk" },
    ],
    course: 3,
    faculty: "Факультет прикладной математики",
}

export const mockMentorDTO: z.infer<typeof mentorDTOschema> = {
    username: "MiniMentor",
    full_name: "Кирилл Лёгкий",
    services: [
        {
            id: 1,
            name: "курсач",
        },
        {
            id: 2,
            name: "диплом",
        },
    ],
    subjects: [
        {
            id: 1,
            name: "сопромат",
        },
        {
            id: 2,
            name: "вышмат",
        },
    ],
    rating: 4.7,
    photo: "https://example.com/avatar.jpg",
    count_successful_transactions: 5,
}

export const mockMentorsDTO: z.infer<ReturnType<typeof mentorDTOschema.array>> =
    [
        mockMentorDTO,
        {
            username: "NoobHelper",
            full_name: "1234",
            services: [
                {
                    id: 1,
                    name: "курсач",
                },
                {
                    id: 2,
                    name: "диплом",
                },
            ],
            subjects: [
                {
                    id: 1,
                    name: "сопромат",
                },
                {
                    id: 2,
                    name: "вышмат",
                },
            ],
            rating: 3.9,
            photo: null,
            count_successful_transactions: 0,
        },
    ]

export const mockMentorModel: MentorModel = {
    username: "MiniMentor",
    fullName: "Кирилл Лёгкий",
    services: [
        { id: 1, name: "курсач" },
        { id: 2, name: "диплом" },
    ],
    subjects: [
        { id: 1, name: "предметы" },
        { id: 2, name: "сопромат" },
    ],
    rating: 4.7,
    photo: "https://example.com/avatar.jpg",
    countSuccessfulTransactions: 5,
}

export const mockMentorsModel: MentorModel[] = [
    mockMentorModel,
    {
        username: "NoobHelper",
        fullName: "321",
        services: [],
        subjects: [],
        rating: 3.9,
        photo: null,
        countSuccessfulTransactions: 0,
    },
]
