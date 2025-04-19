import { clsx } from "clsx"
import { MentorModel } from "../model"
import classes from "./mentor.module.scss"

export function MentorCard({ mentor }: { mentor: MentorModel }) {
    return (
        <article className={classes.mentorCard}>
            <div className={classes.main}>
                <img
                    className={classes.image}
                    src={mentor.photo}
                    alt='mentor image'
                    width='95'
                    height='120'
                    loading='lazy'
                />
                <div className={classes.info}>
                    <div className={classes.row}>
                        <h2 className={classes.name}>{mentor.fullName}</h2>
                        <div className={classes.rating}>
                            <p>рейтинг:{mentor.rating}</p>
                        </div>
                    </div>
                    <div className={clsx(classes.row, classes.tags)}>
                        <p>
                            {mentor.countSuccessfulTransactions} завершенных
                            сделок
                        </p>
                    </div>
                    <div className={classes.row}>
                        {mentor.subjects.map((el) => (
                            <span key={el.id}>{el.name}</span>
                        ))}
                    </div>
                </div>
            </div>
            <div className={clsx(classes.typeTags, classes.tags)}>
                {mentor.services.map((el) => (
                    <span key={el.id}>{el.name}</span>
                ))}
            </div>
        </article>
    )
}
