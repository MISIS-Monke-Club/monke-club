import React from "react"
import "./Button.scss"

type ButtonProps = {
    children?: React.ReactNode
    variant?: "primary" | "secondary" | "danger" | "disabled"
    size?: "sm" | "lg"
    isLoading?: boolean
    isIcon?: boolean
    className?: string
    onClick?: () => void
    type?: "button" | "submit"
}

export const Button = ({
    children,
    variant = "primary",
    size,
    isLoading = false,
    isIcon = false,
    className = "",
    onClick,
    type = "button",
}: ButtonProps) => {
    const classes = [
        "btn",
        `btn--${variant}`,
        size && `btn--${size}`,
        isLoading && "btn--loading",
        isIcon && "btn--icon",
        className,
    ]
        .filter(Boolean)
        .join(" ")

    return (
        <button
            type={type}
            className={classes}
            onClick={onClick}
            disabled={isLoading}
        >
            {isLoading ? "Загрузка..." : children}
        </button>
    )
}
