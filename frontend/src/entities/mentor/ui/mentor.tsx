import { clsx } from "clsx"
import { useNavigate } from "react-router-dom"
import { MentorModel } from "../model/domain"
import { api } from "../api"
import classes from "./mentor.module.scss"
import { Tag } from "@shared/ui/tag"

export function MentorCard({ mentor }: { mentor: MentorModel }) {
    const navigate = useNavigate()

    function clickHandler() {
        navigate(`/${api.baseUrl}/${mentor.username}`)
    }

    return (
        <article className={classes.mentorCard} onClick={clickHandler}>
            <div className={classes.main}>
                <img
                    className={classes.image}
                    src={mentor.photo || ""}
                    alt='mentor image'
                    width='95'
                    height='120'
                    loading='lazy'
                />
                <div className={classes.info}>
                    <div className={classes.row}>
                        <h2 className={classes.name}>
                            {mentor.fullName.length !== 0
                                ? mentor.fullName
                                : "Неизвестный пользователь"}
                        </h2>
                        <div className={classes.rating}>
                            <p>
                                <span>⭐</span>
                                <span>{mentor.rating}</span>
                            </p>
                        </div>
                    </div>
                    <div className={classes.row}>
                        <p>
                            {mentor.countSuccessfulTransactions} завершенных
                            сделок
                        </p>
                    </div>
                    <div className={clsx(classes.row, classes.subjects)}>
                        {mentor.subjects.map((el) => (
                            <Tag key={el.id} variants='subject'>
                                {el.name}
                            </Tag>
                        ))}
                    </div>
                </div>
            </div>
            <div className={clsx(classes.typeTags, classes.services)}>
                {mentor.services.map((el) => (
                    <Tag key={el.id} variants='type'>
                        {el.name}
                    </Tag>
                ))}
            </div>
        </article>
    )
}
