type ButtonProps = React.ComponentProps<"button"> & {}

export function Button({ ...rest }: ButtonProps) {
    return <button type='button' {...rest} />
}
