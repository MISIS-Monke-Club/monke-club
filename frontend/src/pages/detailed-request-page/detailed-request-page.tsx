import { useParams } from "react-router-dom"
import { useQuery } from "@tanstack/react-query"
import classes from "./detailed-request-page.module.scss"
import { api } from "@features/request/by-id"
import { FullRequestModel } from "@features/request/by-id"

export function RequestDetail() {
    const { slug } = useParams<{ slug: string }>()

    const { data, isLoading, isError } = useQuery<FullRequestModel>(
        api.getRequestBySlug(slug!)
    )

    if (isLoading) return <div>Загрузка...</div>
    if (isError) return <div>Ошибка при загрузке заявки</div>
    if (!data) return <div>Заявка не найдена</div>

    return (
        <div className={classes.div}>
            <h1>{data.name}</h1>
            <p>{data.description}</p>
            <p>Цена: {data.price}</p>
        </div>
    )
}
