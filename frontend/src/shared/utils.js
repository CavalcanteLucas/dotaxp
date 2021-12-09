export function range(start, end) {
    return Array.from(Array(end || start).keys()).slice(!!end * start)
}

export function transpose(a) {
    return a[0].map((_, c) => a.map(r => r[c]))
}