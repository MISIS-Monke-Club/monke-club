import { z } from "zod"

export const requestDTOschema = z.object({
    name: z.string(),
    username: z.string(),
    year: z.number().nullable(),
    subjects: z.array(
        z.object({
            id: z.number(),
            name: z.string(),
        })
    ),
    services: z.array(
        z.object({
            id: z.number(),
            name: z.string(),
        })
    ),
    date_of_creation: z.string().nullable(),
    price: z.string().nullable(),
    slug: z.string(),
})

export const requestListDTOschema = z.array(requestDTOschema)

export type RequestDTO = z.infer<typeof requestDTOschema>

export type RequestModel = {
    name: string
    username: string
    year: number | null
    subjects: string[]
    services: string[]
    createdAt: Date | null
    price: number | null
    slug: string
}

export function fromRequestDTO(dto: RequestDTO): RequestModel {
    return {
        name: dto.name,
        username: dto.username,
        year: dto.year,
        subjects: dto.subjects.map((s) => s.name),
        services: dto.services.map((s) => s.name),
        createdAt: dto.date_of_creation ? new Date(dto.date_of_creation) : null,
        price: dto.price ? parseFloat(dto.price) : null,
        slug: dto.slug,
    }
}
