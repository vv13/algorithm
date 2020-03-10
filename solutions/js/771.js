/**
 * @param {string} J
 * @param {string} S
 * @return {number}
 */
var numJewelsInStones = function (J, S) {
    let count = 0
    S.split('').forEach(s => {
        if (J.includes(s)) count += 1
    })
    return count
}
