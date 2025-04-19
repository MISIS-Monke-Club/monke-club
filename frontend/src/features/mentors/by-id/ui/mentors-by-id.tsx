import { useQuery } from "@tanstack/react-query"
import { getMentorById } from "../api"
import classes from "./mentors-by-id.module.scss"
import { MentorId } from "@entities/mentor"
// TODO: create
import { Rating } from "@shared/rating"

export function MentorById({ username }: MentorId) {
    const { data: mentor, isLoading } = useQuery(getMentorById({ username }))

    if (isLoading) {
        return <div>Загрузка...</div>
    }

    if (!mentor) {
        return <div>Что-то пошло не так</div>
    }

    return (
        <>
            <div className={classes.mainInfo}>
                <img
                    className={classes.image}
                    src={mentor.photo}
                    alt='mentor image'
                    width='160'
                    height='140'
                    loading='lazy'
                />
                <h2 className={classes.name}>{mentor.fullName}</h2>
                <div className={classes.username}>
                    <p>{mentor.username}</p>
                </div>
                <div className={classes.rating}>
                    <Rating rating={mentor.rating} />
                </div>
                <div className={classes.university}>
                    <span>
                        <p>{mentor.fullName}</p>
                    </span>
                    <span>
                        <p>{mentor.fullName}</p>
                    </span>
                </div>
            </div>
        </>
    )
}
