import { createSlice, PayloadAction } from "@reduxjs/toolkit"

type State = {
    userId: string | null
    users: Record<string, string>
}

const initialState: State = {
    userId: null,
    users: {},
}

export const sessionSlice = createSlice({
    name: "session",
    initialState,
    reducers: {
        setUserId: (state, action: PayloadAction<{ userId: string }>) => {
            const { userId } = action.payload

            state.userId = userId
        },
        register: (
            state,
            action: PayloadAction<{ userId: string; password: string }>
        ) => {
            const { userId, password } = action.payload

            state.users[userId] = password
        },
    },
    selectors: {
        selectUserId: (state) => state.userId,
    },
})

export const { setUserId, register } = sessionSlice.actions
export const { selectUserId } = sessionSlice.selectors
