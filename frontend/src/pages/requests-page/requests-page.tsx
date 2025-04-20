import { useQuery } from "@tanstack/react-query"
import { Link } from "react-router-dom"
import classes from "./requests-page.module.scss"
import { api } from "@features/request/list"
import { RequestModel } from "@features/request/list"
import { RequestCard } from "@features/request/request-card/request-card"

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
            <div className={classes.grid}>
                {data?.map((request) => (
                    <Link
                        to={`/request/${request.slug}`}
                        className={classes.link}
                    >
                        <RequestCard key={request.name} request={request} />
                    </Link>
                ))}
            </div>
        </>
    )
}
