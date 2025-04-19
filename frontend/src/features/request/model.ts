import { z } from 'zod'

export const requestDTOschema = z.object({
    id: z.string(),
    title: z.string(),
})

export const requestListDTOschema = z.array(requestDTOschema)

export type RequestDTO = z.infer<typeof requestDTOschema>

export type RequestModel = {
    id: string
    title: string
}

export const fromRequestDTO = (dto: RequestDTO): RequestModel => ({
    id: dto.id,
    title: dto.title,
})