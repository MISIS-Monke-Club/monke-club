import z from "zod"

export const fullRequestDTOschema = z.object({
    id: z.number(),
    name: z.string(),
    slug: z.string(),
    year: z.number(),
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
    date_of_creation: z.string(),
    description: z.string(),
    price: z.string(),
    is_finished: z.boolean(),
    file: z.string().url(),
    user: z.number(),
    executor_id: z.number(),
})

export type FullRequestDTO = z.infer<typeof fullRequestDTOschema>

export type FullRequestModel = {
    id: number
    name: string
    slug: string
    year: number
    subjects: string[]
    services: string[]
    createdAt: Date
    description: string
    price: number
    isFinished: boolean
    file: string
    user: number
    executorId: number
}

export function fromFullRequestDTO(dto: FullRequestDTO): FullRequestModel {
    return {
        id: dto.id,
        name: dto.name,
        slug: dto.slug,
        year: dto.year,
        subjects: dto.subjects.map((s) => s.name),
        services: dto.services.map((s) => s.name),
        createdAt: new Date(dto.date_of_creation),
        description: dto.description,
        price: parseFloat(dto.price),
        isFinished: dto.is_finished,
        file: dto.file,
        user: dto.user,
        executorId: dto.executor_id,
    }
}
