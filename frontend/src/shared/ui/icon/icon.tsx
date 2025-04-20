import clsx from "clsx"
import classes from "./icon.module.scss"

type IconProps = {
    data: number | string
    src?: string
    withLabel?: boolean
    iconPosition?: "before" | "after"
    size?: "lg" | "sm"
}

export const Icon = ({
    data,
    iconPosition = "before",
    src = "",
    withLabel = false,
    size = "sm",
}: IconProps) => {
    const spanClass = clsx({
        [classes.lg]: size === "lg",
    })

    if (withLabel) {
        if (iconPosition === "before") {
            return (
                <div className={classes.wrapper}>
                    <img src={src} />
                    <span className={spanClass}>{data}</span>
                </div>
            )
        } else {
            return (
                <div className={classes.wrapper}>
                    <span className={spanClass}>{data}</span>
                    <img src={src} />
                </div>
            )
        }
    } else {
        return (
            <div className={classes.wrapper}>
                <span className={spanClass}>{data}</span>
            </div>
        )
    }
}
