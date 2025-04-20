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
            <p>
                <strong>Описание:</strong> {data.description}
            </p>
            <p>
                <strong>Цена:</strong> {data.price}
            </p>
            <p>
                <strong>Год:</strong> {data.year}
            </p>
            <p>
                <strong>Статус:</strong>{" "}
                {data.isFinished ? "Завершено" : "Не завершено"}
            </p>
            <p>
                <strong>Файл:</strong>{" "}
                {data.file ? (
                    <a
                        href={data.file}
                        target='_blank'
                        rel='noopener noreferrer'
                    >
                        Скачать
                    </a>
                ) : (
                    "Нет файла"
                )}
            </p>
            <p>
                <strong>Пользователь:</strong> {data.user}
            </p>
            <p>
                <strong>Исполнитель:</strong> {data.executorId ?? "Не указан"}
            </p>
            <p>
                <strong>Предметы:</strong>{" "}
                {data.subjects.length > 0
                    ? data.subjects.join(", ")
                    : "Нет предметов"}
            </p>
            <p>
                <strong>Услуги:</strong>{" "}
                {data.services.length > 0
                    ? data.services.join(", ")
                    : "Нет услуг"}
            </p>
            <p>
                <strong>Дата создания:</strong>{" "}
                {data.createdAt.toLocaleDateString()}
            </p>
            <p>
                <strong>Слаг:</strong> {data.slug}
            </p>
        </div>
    )
}
