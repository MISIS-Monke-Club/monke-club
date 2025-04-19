import { combineSlices } from "@reduxjs/toolkit"
import { sessionSlice } from "@entities/session"

export const reducer = combineSlices(sessionSlice)
