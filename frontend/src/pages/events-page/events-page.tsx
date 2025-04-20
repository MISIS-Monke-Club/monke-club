import { Link } from "react-router-dom"
import classes from "./events-page.module.scss"

export function EventsPage() {
    return (
        <div className={classes.div}>
            <img className={classes.img} src='/logo-large.png' />
            <div className={classes.text}>
                <span className={classes.first}>
                    Добро пожаловать в нашу афишу студенческих событий!
                </span>
                <span className={classes.second}>
                    Самые выгодные и интересные мероприятиях для студента с
                    любыми интересами и бюджетом вы найдете здесь.
                </span>
                <span className={classes.third}>
                    Собирай друзей и приглашай их на наши мероприятия!
                </span>
            </div>
            <div className={classes.btns}>
                <Link to='/'>
                    <button className={classes.btnMain}>
                        Вперед к интересным ивентам
                    </button>
                </Link>
            </div>
        </div>
    )
}
