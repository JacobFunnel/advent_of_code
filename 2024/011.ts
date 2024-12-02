import * as fs from 'fs'
import * as path from 'path'

const filePath = path.join(__dirname, '/input/011.txt')
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
locA.sort((a, b) => a - b)
locB.sort((a, b) => a - b)
if (locA.length !== locB.length) {
    throw new Error('lists of unequal length')
}
const distances: number[] = []
for (let i = 0; i < locA.length; i++) {
    distances.push(Math.abs(locA[i] - locB[i]))
}
const sum = distances.reduce((a, b) => a + b, 0)
console.log(sum)