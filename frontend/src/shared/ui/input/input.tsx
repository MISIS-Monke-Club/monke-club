import "./Input.scss"

type InputProps = {
    value?: string
    placeholder?: string
    type?: string
    label?: string
    error?: string
    isLoading?: boolean
    disabled?: boolean
    className?: string
}

export const Input = ({
    value,
    placeholder = "",
    type = "text",
    label,
    error,
    isLoading = false,
    disabled = false,
    className = "",
}: InputProps) => {
    const classes = [
        "input-wrapper",
        error && "input-wrapper--error",
        isLoading && "input-wrapper--loading",
        className,
    ]
        .filter(Boolean)
        .join(" ")

    return (
        <div className={classes}>
            {label && <label className='input-label'>{label}</label>}
            <div className='input-inner'>
                <input
                    className='input'
                    type={type}
                    value={value}
                    placeholder={placeholder}
                    disabled={isLoading || disabled}
                />
                {isLoading && disabled}
            </div>
            {error && <span className='input-error'>{error}</span>}
        </div>
    )
}
