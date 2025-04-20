import { Link } from "react-router-dom"
import classes from "./header.module.scss"

export function Header() {
    return (
        <header className={classes.header}>
            <div className={classes.left}>
                <Link to='/'>
                    <img
                        className={classes.logo}
                        src='/logo.svg'
                        alt='logo'
                        width='60'
                        height='60'
                        loading='lazy'
                    />
                </Link>
                <nav className={classes.nav}>
                    <Link to='marketplace' className={classes.navLinks}>
                        Менторы
                    </Link>
                    <Link to='request' className={classes.navLinks}>
                        Заявки на помощь
                    </Link>
                </nav>
            </div>

            <div className={classes.right}>
                <img
                    className={classes.logo}
                    src='/icon-search.svg'
                    alt='logo'
                    width='60'
                    height='60'
                    loading='lazy'
                />
                <img
                    className={classes.logo}
                    src='/icon-profile.svg'
                    alt='logo'
                    width='60'
                    height='60'
                    loading='lazy'
                />
            </div>
        </header>
    )
}
