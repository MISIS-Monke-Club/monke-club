import classes from "./icon.module.scss"

type IconProps = {
    data: number | string
    src?: string
    withLabel?: boolean
    iconPosition?: "before" | "after"
}

export const Icon = ({
    data,
    iconPosition = "before",
    src = "",
    withLabel = false,
}: IconProps) => {
    if (withLabel) {
        if (iconPosition === "before") {
            return (
                <div className={classes.wrapper}>
                    <img src={src} />
                    <span>{data}</span>
                </div>
            )
        } else {
            return (
                <div className={classes.wrapper}>
                    <span>{data}</span>
                    <img src={src} />
                </div>
            )
        }
    } else {
        return (
            <div className={classes.wrapper}>
                <span>{data}</span>
            </div>
        )
    }
}
