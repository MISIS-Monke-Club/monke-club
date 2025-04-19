import { createSlice, PayloadAction } from "@reduxjs/toolkit"

type State = {
    userId: string | null
}

const initialState: State = {
    userId: null,
}

export const sessionSlice = createSlice({
    name: "session",
    initialState,
    reducers: {
        setUserId: (state, action: PayloadAction<{ userId: string }>) => {
            const { userId } = action.payload

            state.userId = userId
        },
    },
    selectors: {
        selectUserId: (state) => state.userId,
    },
})

export const { setUserId } = sessionSlice.actions
export const { selectUserId } = sessionSlice.selectors
