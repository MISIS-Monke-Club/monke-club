import { RequestModel } from "../list"
import classes from "./request-card.module.scss"
import { Tag } from "@shared/ui/tag"
import { Icon } from "@shared/ui/icon"

type RequestCardProp = {
    request: RequestModel
}

export function RequestCard({ request }: RequestCardProp) {
    return (
        <>
            <div className={classes.card}>
                <div className={classes.header}>
                    <span className={classes.title}>{request.name}</span>
                    <Icon
                        data={Number(request.price)}
                        withLabel
                        iconPosition='after'
                        src='/icon-ruble.svg'
                    />
                </div>
                <span className={classes.year}>{request.year} курс</span>
                <div className={classes.tags}>
                    {request.subjects.length > 0
                        ? request.subjects.map((subject) => (
                              <Tag
                                  key={subject}
                                  text={subject}
                                  variants='subject'
                              />
                          ))
                        : ""}
                    {request.services.length > 0
                        ? request.services.map((services) => (
                              <Tag
                                  key={services}
                                  text={services}
                                  variants='type'
                              />
                          ))
                        : ""}
                </div>
                <div className={classes.date}>
                    {request.createdAt
                        ? new Date(request.createdAt).toLocaleDateString()
                        : ""}
                </div>
            </div>
        </>
    )
}
