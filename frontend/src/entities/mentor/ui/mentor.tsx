import { MentorModel } from "../model"

export function MentorCard({ mentor }: { mentor: MentorModel }) {
    return <article>{mentor.fullName}</article>
}
