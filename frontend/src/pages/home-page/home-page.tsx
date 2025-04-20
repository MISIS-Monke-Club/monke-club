import { Link } from "react-router-dom"
import classes from "./home-page.module.scss"

export function Homepage() {
    return (
        <>
            <h1 className={classes.title}>
                Открой заново мир студенчества с хабом от MISIS Monke Club!
            </h1>
            <div className={classes.largeCard}>
                <img src='/mentors.png' alt='' />
                <span className={classes.cardTitle}>Менторство</span>
                <span className={classes.desc}>
                    Найдите ментора, станьте ментором или оставьте заявку, чтобы
                    вам помогли с курсовой, лабораторной или любой другой
                    учебной работой. Ментор станет надежным помощником в трудных
                    ситуациях.
                </span>
                <Link to='/marketplace'>
                    <button className={classes.button}>Перейти</button>
                </Link>
            </div>
            <div className={classes.wrapper}>
                <div className={classes.smCard}>
                    <img src='/events.png' alt='' />
                    <span className={classes.cardTitle}>События</span>
                    <span className={classes.desc}>
                        Не знаете, куда сходить на выходные с друзьями?
                        Проведите время с пользой и посетите самые интересные
                        студенческие мероприятия этого сезона!
                    </span>
                    <Link to='/events'>
                        <button className={classes.button}>Перейти</button>
                    </Link>
                </div>
                <div className={classes.smCard}>
                    <img src='/vacations.png' alt='' />
                    <span className={classes.cardTitle}>Вакансии</span>
                    <span className={classes.desc}>
                        Найдите работу мечты от проверенных работодателей и
                        других студентов. Лучшие предложения, которые невозможно
                        найти ни на одной другой платформе.
                    </span>
                    <Link to='/vacations'>
                        <button className={classes.button}>Перейти</button>
                    </Link>
                </div>
            </div>
        </>
    )
}
