package main

import (
	"fmt"
	"strings"

	parse "github.com/dratzinger/Advent-of-Code/2021/util"
)

func main() {
	in := parse.StrLines("input.txt")
	fmt.Println("Day 5 - Pt. 1:", Part1(in))
	fmt.Println("Day 5 - Pt. 2:", Part2(in))
}

type point struct {
	x, y int
}

type line struct {
	start, end point
}

func Part1(input []string) int {
	lines, xMax, yMax := makeLines(input)
	chart := initChart(xMax+1, yMax+1)

	for _, line := range lines {
		if line.start.x == line.end.x || line.start.y == line.end.y {
			drawLine(chart, line)
		}
	}
	return count(&chart, 2)
}

func Part2(input []string) int {
	lines, xMax, yMax := makeLines(input)
	chart := initChart(xMax+1, yMax+1)

	for _, line := range lines {
		drawLine(chart, line)
	}

	return count(&chart, 2)
}

func makeLines(input []string) (lines []line, maxX, maxY int) {
	for _, instruction := range input {
		if instruction != "" {
			str := strings.ReplaceAll(instruction, " -> ", ",")
			data := strings.Split(str, ",")
			coords := parse.IntSlice(data)
			line := line{
				start: point{coords[0], coords[1]},
				end:   point{coords[2], coords[3]},
			}
			maxX = max(line.start.x, line.end.x, maxX)
			maxY = max(line.start.y, line.end.y, maxY)
			lines = append(lines, line)
		}
	}
	return lines, maxX, maxY
}

func initChart(xDim, yDim int) [][]int {
	chart := make([][]int, yDim)
	for i := range chart {
		chart[i] = make([]int, xDim)
	}
	return chart
}

func orthogonalLine(chart [][]int, line line) [][]int {
	xMin := min(line.start.x, line.end.x)
	xMax := max(line.start.x, line.end.x)

	yMin := min(line.start.y, line.end.y)
	yMax := max(line.start.y, line.end.y)

	for y := range chart {
		for x := range chart {
			horizontal := x == line.start.x && (yMin <= y && y <= yMax)
			vertical := y == line.start.y && (xMin <= x && x <= xMax)

			if vertical || horizontal {
				chart[y][x]++
			}
		}
	}
	return chart
}

func drawLine(chart [][]int, line line) [][]int {

	setPixel := func(x, y int) {
		chart[y][x]++
	}

	// bresenham comin' straight from the wikipedia
	bresenham := func(x0, y0, x1, y1 int) {
		dx := Abs(x1 - x0)
		dy := -Abs(y1 - y0)

		var sx int
		if x0 < x1 {
			sx = 1
		} else {
			sx = -1
		}

		var sy int
		if y0 < y1 {
			sy = 1
		} else {
			sy = -1
		}

		err := dx + dy

		for {
			setPixel(x0, y0)
			if x0 == x1 && y0 == y1 {
				break
			}

			e2 := 2 * err

			if e2 > dy {
				err += dy
				x0 += sx
			}

			if e2 < dx {
				err += dx
				y0 += sy
			}
		}
	}

	bresenham(line.start.x, line.start.y, line.end.x, line.end.y)
	return chart
}

func Abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}

func min(vals ...int) int {
	min := vals[0]
	for _, v := range vals {
		if v < min {
			min = v
		}
	}
	return min
}

func max(vals ...int) int {
	max := vals[0]
	for _, v := range vals {
		if v > max {
			max = v
		}
	}
	return max
}

func count(chart *[][]int, threshold int) (count int) {
	for _, line := range *chart {
		for _, val := range line {
			if val >= threshold {
				count++
			}
		}
	}
	return count
}
