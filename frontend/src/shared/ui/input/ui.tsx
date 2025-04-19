type InputProps = React.ComponentProps<"input"> & {}

export function Input({ ...rest }: InputProps) {
    return <input type='text' {...rest} />
}
