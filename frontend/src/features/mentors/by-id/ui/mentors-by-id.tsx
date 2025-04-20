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
                        <h3 className={classes.value}>
                            <span>Завершенные сделки: </span>
                            <span>{mentor.countSuccessfulTransactions}</span>
                        </h3>
                        <div className={classes.bg} />
                    </div>
                    <div className={classes.person}>
                        <div className={classes.info}>
                            <div className={classes.about}>
                                <div className={classes.text}>
                                    <h2 className={classes.name}>
                                        {mentor.fullName || "Неизвестное имя"}
                                    </h2>
                                    <p>
                                        <span>@</span>
                                        <span>{mentor.username}</span>
                                    </p>
                                </div>
                                <Rating rating={mentor.rating} />
                            </div>
                            <div className={classes.university}>
                                <Tag className={classes.tag}>
                                    <p>
                                        <span>{mentor.course}</span>
                                        <span> Курс</span>
                                    </p>
                                </Tag>
                                <Tag className={classes.tag}>
                                    {mentor.faculty}
                                </Tag>
                            </div>
                        </div>
                    </div>
                    <div className={classes.bio}>
                        <h3 className={classes.title}>Описание</h3>
                        <p>{mentor.description}</p>
                    </div>
                </div>
            </div>
            <div className={classes.additionInfo}>
                <div className={classes.tags}>
                    <div className={classes.tagGroup}>
                        <h4 className={classes.title}>Услуги</h4>
                        <div className={classes.list}>
                            {mentor.services.length !== 0
                                ? mentor.services.map((el) => (
                                      <Tag key={el.id}>{el.name}</Tag>
                                  ))
                                : "Отсутствуют"}
                        </div>
                    </div>
                    <div className={classes.tagGroup}>
                        <h4 className={classes.title}>Дисциплины</h4>
                        <div className={classes.list}>
                            {mentor.subjects.length !== 0
                                ? mentor.subjects.map((el) => (
                                      <Tag key={el.id}>{el.name}</Tag>
                                  ))
                                : "Отсутствуют"}
                        </div>
                    </div>
                </div>
                <div className={classes.contacts}>
                    <h4 className={classes.title}>Контакты</h4>
                    <div className={classes.list}>
                        {mentor.socialNetwork.length !== 0
                            ? mentor.socialNetwork.map((el) => (
                                  <Tag key={crypto.randomUUID()}>{el.name}</Tag>
                              ))
                            : "Отсутствуют"}
                    </div>
                </div>
            </div>
        </>
    )
}
