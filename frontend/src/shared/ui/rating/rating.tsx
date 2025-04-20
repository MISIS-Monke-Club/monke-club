import { ReactNode } from "react"
import React from "react"
import classes from "./rating.module.scss"

type RatingProps = {
    rating: number
    component?: ReactNode
}

export function Rating({
    rating,
    component = (
        <img
            className='class-for-img'
            src='/star-icon.svg'
            alt='star icon'
            width='25'
            height='16'
            loading='lazy'
        />
    ),
}: RatingProps) {
    if (rating < 0.5) {
        return (
            <div className={classes.value}>
                <p>Рейтинг: {rating}</p>
            </div>
        )
    }
    return (
        <div className={classes.wrapper}>
            {rating >= 0.5 &&
                Array.from({ length: Math.round(rating) }).map(() => (
                    <React.Fragment key={crypto.randomUUID()}>
                        {component}
                    </React.Fragment>
                ))}
            <div className={classes.value}>
                <p>{rating}</p>
            </div>
        </div>
    )
}
