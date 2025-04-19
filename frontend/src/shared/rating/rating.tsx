import classes from "./rating.module.scss"

export function Rating({ rating }: { rating: number }) {
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
                    <span>+</span>
                ))}
            <div className={classes.value}>
                <p>{rating}</p>
            </div>
        </div>
    )
}
