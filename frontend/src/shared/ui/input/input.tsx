import clsx from "clsx"
import "./Input.scss"
import { ChangeEvent } from "react"

type InputProps = {
    value?: string
    onChange?: (e: ChangeEvent<HTMLInputElement>) => void
    placeholder?: string
    type?: string
    label?: string
    error?: string
    isLoading?: boolean
    disabled?: boolean
    className?: string
}

export const Input = ({
    value = "",
    onChange,
    placeholder = "",
    type = "text",
    label,
    error,
    isLoading = false,
    disabled = false,
    className,
}: InputProps) => {
    const wrapperClass = clsx(
        "wrapper",
        error && "error",
        isLoading && "loading",
        className
    )

    return (
        <div className={wrapperClass}>
            {label && <label className='label'>{label}</label>}

            <div className='inner'>
                <input
                    className='input'
                    type={type}
                    value={value}
                    onChange={onChange}
                    placeholder={placeholder}
                    disabled={disabled || isLoading}
                />
                {isLoading && <div className='loader' />}
            </div>

            {error && <span className='ierror'>{error}</span>}
        </div>
    )
}
