import clsx from "clsx"
import classes from "./tag.module.scss"

type TagProps = {
    text: string
    variants?: "subject" | "type" | "secondary"
}

export const Tag = ({ text, variants = "subject" }: TagProps) => {
    const combinedClassNames = clsx(classes.tag, classes[variants])
    return <div className={combinedClassNames}>{text}</div>
}
