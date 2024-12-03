import * as fs from 'fs'
import * as path from 'path'

const filePath = path.join(__dirname, '/input/02.txt')
const fileContent = fs.readFileSync(filePath, 'utf-8')
const lines = fileContent.split('\n').slice(0, -1)
let reports: Array<Array<number>> = []
lines.forEach((line) => {
    reports.push(line.split(' ').map((n) => parseInt(n)))
})

function pairWise(arr: number[]) {
    return arr.slice(1).map((k, i) => [arr[i], k])
}
let differences: number[]
let min: number
let max: number
let safeReports = 0
reports.forEach((report) => {
    differences = []
    pairWise(report).forEach((pair) => {
        const [a, b] = pair
        differences.push(a - b)
    })
    min = Math.min(...differences)
    max = Math.max(...differences)
    if (differences.every((n) => n > 0)) {
        if (min >= 1 && max <= 3)
            safeReports++
    }
    if (differences.every((n) => n < 0)) {
        if (max <= -1 && min >= -3)
            safeReports++
    }
})
console.log(safeReports)
