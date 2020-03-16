const reverse = (x) => {
  const number = parseInt(
    (x > 0 ? '' : '-') +
      Math.abs(x)
        .toString()
        .split('')
        .reverse()
        .join('')
  )
  if (Math.abs(number) >= 2147483647) return 0
  return number
}
