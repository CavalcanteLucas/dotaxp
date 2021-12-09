export function range(start, end) {
    return Array.from(Array(end || start).keys()).slice(!!end * start)
}
