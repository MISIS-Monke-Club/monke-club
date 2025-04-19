import { Link } from "react-router-dom"
import classes from "./home-page.module.scss"

export function Homepage() {
    return (
        <section className={classes.landingSection}>
            <div className={classes.main}>
                <div className={classes.header}>
                    <h1 className={classes.title}>Добро пожаловать на сайт</h1>
                </div>
                <img
                    className={classes.previewImage}
                    src='/preview-image.jpg'
                    alt='preview image'
                    width='300'
                    height='300'
                    loading='lazy'
                />
            </div>
            <Link to='/grenades'>Найти раскидку для себя</Link>
        </section>
    )
}
