import { Link } from "react-router-dom"
import classes from "./header.module.scss"

export function Header() {
    return (
        <header className={classes.header}>
            <img
                className={classes.logo}
                src='/'
                alt='logo'
                width='150'
                height='150'
                loading='lazy'
            />
            <nav>
                <Link to='/'>Homepage</Link>
                <Link to='marketplace'>Marketplace</Link>
            </nav>
            <div className={classes.actions}></div>
        </header>
    )
}
