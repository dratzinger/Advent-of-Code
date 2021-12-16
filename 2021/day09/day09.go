package main

import (
	"fmt"
	"sort"

	"github.com/dratzinger/Advent-of-Code/2021/util/parse"
)

type point struct {
	x, y int
}

func main() {
	in := parse.StrLines("input.txt")
	fmt.Println("Day 9 - Pt. 1:", Part1(in))
	fmt.Println("Day 9 - Pt. 2:", Part2(in))
}

func Part1(input []string) (risk int) {
	heightMap, lowPoints := crunch(input)
	for _, p := range lowPoints {
		risk += 1 + heightMap[p.y][p.x]
	}
	return risk
}

func Part2(input []string) (count int) {
	heightMap, lowPoints := crunch(input)

	basins := []int{}
	for _, v := range lowPoints {
		sum := FloodSum(heightMap, v.x, v.y)
		basins = append(basins, sum)
	}
	// sort the basins
	sort.IntSlice(basins).Sort()
	topThree := basins[len(basins)-3:]

	for _, v := range topThree {
		count += v
	}
	return count
}

func crunch(input []string) (heightMap [][]int, lowPoints []point) {
	heightMap = makeHeightmap(input)
	lowPoints = findLowPoints(heightMap)
	return heightMap, lowPoints
}

var directions func(int, int) [][]int

func makeHeightmap(input []string) (heights [][]int) {
	heights = parse.IntMatrix(input)
	directions = makeDirectionFn(len(heights[0])-1, len(heights)-1)
	return heights
}

func makeDirectionFn(maxX, maxY int) func(int, int) [][]int {
	var dirFn = func(x, y int) (directions [][]int) {
		if x != 0 {
			directions = append(directions, []int{-1, 0})
		}
		if x != maxX {
			directions = append(directions, []int{1, 0})
		}
		if y != 0 {
			directions = append(directions, []int{0, -1})
		}
		if y != maxY {
			directions = append(directions, []int{0, 1})
		}
		return directions
	}
	return dirFn
}

func findLowPoints(heights [][]int) (lowPoints []point) {
	for y, row := range heights {
		for x, height := range row {
			var isLowPoint = func(heights [][]int, x, y int) bool {
				for _, direction := range directions(x, y) {
					if heights[y+direction[1]][x+direction[0]] <= height {
						return false
					}
				}
				return true
			}

			if isLowPoint(heights, x, y) {
				lowPoints = append(lowPoints, point{x, y})
			}
		}
	}
	return lowPoints
}

func FloodSum(heights [][]int, x, y int) (sum int) {
	sum += heights[y][x]
	heights[y][x] = 0
	for _, direction := range directions(x, y) {
		if heights[y+direction[1]][x+direction[0]] != 9 {
			sum += FloodSum(heights, x+direction[0], y+direction[1])
		}
	}
	return sum
}
