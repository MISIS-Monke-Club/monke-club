import clsx from "clsx"
import classes from "./tag.module.scss"

type TagProps = React.ComponentProps<"span"> & {
    variants?: "subject" | "type"
}

export const Tag = ({ variants = "subject", className, ...rest }: TagProps) => {
    const combinedClassNames = clsx(classes.tag, classes[variants])

    return <span className={combinedClassNames} {...rest} />
}
