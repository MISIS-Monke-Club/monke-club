import { sessionSlice } from "@entities/session"
import { combineSlices } from "@reduxjs/toolkit"

export const reducer = combineSlices(sessionSlice)
