import { useQuery } from "@tanstack/react-query"
import { getMentorById } from "../api"
import classes from "./mentors-by-id.module.scss"
import { MentorId } from "@entities/mentor"
// TODO: create
import { Rating } from "@shared/ui/rating"
import { Tag } from "@shared/ui/tag"

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
            <div className={classes.info}>
                <img
                    className={classes.image}
                    src={mentor.photo || ""}
                    alt='mentor image'
                    width='325'
                    height='440'
                    loading='lazy'
                />
                <div className={classes.main}>
                    <div className={classes.finishedTasks}>
                        <span>{mentor.countSuccessfulTransactions}</span>
                        <div className={classes.finishedBg} />
                    </div>
                    <div className={classes.person}>
                        <div className={classes.info}>
                            <div className={classes.about}>
                                <div className={classes.text}>
                                    <h2 className={classes.name}>
                                        {mentor.fullName}
                                    </h2>
                                    <p>{mentor.username}</p>
                                </div>
                                <Rating rating={mentor.rating} />
                            </div>
                            <div className={classes.university}>
                                <Tag className={classes.tag}>
                                    {mentor.course}
                                </Tag>
                                <Tag className={classes.tag}>
                                    {mentor.faculty}
                                </Tag>
                            </div>
                        </div>
                        <div className={classes.rating}>
                            <Rating rating={mentor.rating} />
                        </div>
                    </div>
                    <div className={classes.bio}>
                        <h3 className={classes.title}>Описание</h3>
                        <p>{mentor.username}</p>
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
            </div>
        </>
    )
}
