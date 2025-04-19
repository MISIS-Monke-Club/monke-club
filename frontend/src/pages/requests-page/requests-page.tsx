import { Header } from "@app/layout/header/header"
import classes from "./requests-page.module.scss"
import { Icon } from "@shared/ui/icon"
import { Tag } from "@shared/ui/tag"

export function RequestsPage() {
    return (
        <>
            <Header/>
            <h1 className={classes.title}>Request Page</h1>
            <p>This is the request page.</p>
            <Icon src="/Ruble.svg" data={12}></Icon>
            <Tag variants="subject" text={"Вышмат"}/>
        </>
    )
}
