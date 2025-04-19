import { useQuery } from "@tanstack/react-query"
import classes from "./requests-page.module.scss"
import { api } from "@features/request"
import { RequestModel } from "@features/request"

export function RequestsPage() {
    const { data, isLoading, isError } = useQuery<RequestModel[]>(
        api.getAllRequests()
    )

    if (isLoading) {
        return <div>Loading...</div>
    }

    if (isError) {
        return <div>Error loading requests</div>
    }

    return (
        <>
            <h1 className={classes.title}>Request Page</h1>
            <p>This is the request page.</p>
            {data?.map((request) => (
                <div key={request.name} className={classes.request}>
                    <h3>{request.name}</h3>
                    <p>Пользователь: {request.username}</p>
                    <p>
                        Цена:{" "}
                        {request.price
                            ? request.price.toFixed(2)
                            : "Не указана"}
                    </p>
                    <p>Год: {request.year ?? "Не указан"}</p>
                    <p>
                        Создано:{" "}
                        {request.createdAt
                            ? request.createdAt.toLocaleDateString()
                            : "Не указано"}
                    </p>

                    <div>
                        <strong>Предметы:</strong>{" "}
                        {request.subjects.length > 0
                            ? request.subjects.join(", ")
                            : "Нет предметов"}
                    </div>
                    <div>
                        <strong>Услуги:</strong>{" "}
                        {request.services.length > 0
                            ? request.services.join(", ")
                            : "Нет услуг"}
                    </div>
                </div>
            ))}
        </>
    )
}
