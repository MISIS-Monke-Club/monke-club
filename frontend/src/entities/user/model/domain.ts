import { z } from "zod"

export const userDTOschema = z.object({
    id: z.string(),
    name: z.string(),
    login: z.string(),
    password: z.string(),
})

export type UserModel = {
    id: string
    name: string
    login: string
    password: string
}
