import { useQuery } from "@tanstack/react-query"
import { ReactNode } from "react"
import { getMentorsList } from "./api"
import { ItemsList } from "@shared/ui/items-list"
import { MentorCard, MentorModel } from "@entities/mentor"

const mentorsMaper = (elements: MentorModel[]): ReactNode => (
    <>
        {elements.map((el) => (
            <MentorCard key={el.username} mentor={el} />
        ))}
    </>
)

export function MentorsList() {
    const { data = [], isLoading } = useQuery(getMentorsList)

    return (
        <ItemsList
            elements={data}
            mapFunction={mentorsMaper}
            isLoading={isLoading}
        />
    )
}
