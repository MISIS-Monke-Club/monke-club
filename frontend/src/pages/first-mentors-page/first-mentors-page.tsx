import { Link } from "react-router-dom"
import classes from "./first-mentors-page.module.scss"

export function FirstMentors() {
    return (
        <div className={classes.div}>
            <img className={classes.img} src='/logo-large.png' />
            <div className={classes.text}>
                <span className={classes.first}>
                    Добро пожаловать на наш студенческий маркетплейс с
                    менторами!
                </span>
                <span className={classes.second}>
                    Здесь ты можешь найти квалифицированную помощь с любой
                    задачей или оставить заявку, чтобы ментор сам нашёл тебя. А
                    также ты можешь сам стать ментором и помогать студентам.
                </span>
                <span className={classes.third}>
                    Готовься к экзаменам, пиши курсовые и оформляй презентации
                    вместе с нами!
                </span>
            </div>
            <div className={classes.btns}>
                <Link to='/marketplace/mentors'>
                    <button className={classes.btnMain}>Найти ментора</button>
                </Link>
                <Link to='/request'>
                    <button className={classes.btnSecond}>
                        Посмотреть заявки
                    </button>
                </Link>
            </div>
        </div>
    )
}
