import { z } from "zod"
import { userDTOschema, UserModel } from "../model/domain"

export const fromUserDTO = (
    userDTO: z.infer<typeof userDTOschema>
): UserModel => ({
    id: userDTO.id,
    login: userDTO.login,
    name: userDTO.name,
    password: userDTO.password,
})
