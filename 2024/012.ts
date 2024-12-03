import * as fs from 'fs'
import * as path from 'path'

const filePath = path.join(__dirname, '/input/01.txt')
const fileContent = fs.readFileSync(filePath, 'utf-8')
const lines = fileContent.split('\n')
const locA: number[] = []
const locB: number[] = []
lines.forEach((line, index) => {
    const [a, b] = line.split('   ')
    if (!isNaN(parseInt(a))) {
        locA.push(parseInt(a))
    }
    if (!isNaN(parseInt(b))) {
        locB.push(parseInt(b))
    }
})

function frequencies(arr: number[]) {
    return arr.reduce((occurrences: Record<number, number>, v) => {
        occurrences[v] = (occurrences[v] ?? 0) + 1
        return occurrences
    }, {})
}

const freqB = frequencies(locB)
const sum = locA.reduce((acc, v) => acc + v * (freqB[v] ?? 0), 0)
console.log(sum)
