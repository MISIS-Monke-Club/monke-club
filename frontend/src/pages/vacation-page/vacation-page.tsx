import { Link } from "react-router-dom"
import classes from "./vacation-page.module.scss"

export function VacationPage() {
    return (
        <div className={classes.div}>
            <img className={classes.img} src='/logo-large.png' />
            <div className={classes.text}>
                <span className={classes.first}>
                    Добро пожаловать на нашу студенческую ярмарку вакансий!
                </span>
                <span className={classes.second}>
                    Лучшие вакансии от проверенных работодателей с удобным
                    графиком и достойной зп — только здесь.
                </span>
                <span className={classes.third}>
                    Мы поможем найти тебе работу мечты!
                </span>
            </div>
            <div className={classes.btns}>
                <Link to='/'>
                    <button className={classes.btnMain}>
                        Пора искать работу
                    </button>
                </Link>
            </div>
        </div>
    )
}
