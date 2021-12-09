package main

import (
	"fmt"

	"github.com/dratzinger/Advent-of-Code/2021/util/integers"
	"github.com/dratzinger/Advent-of-Code/2021/util/parse"
)

func main() {
	in := parse.StrLines("input.txt")
	fmt.Println("Day 9 - Pt. 1:", Part1(in))
	fmt.Println("Day 9 - Pt. 2:", Part2(in))
}

func Part1(input []string) (count int) {
	heightMap := makeHeightmap(input)
	lowPoints := findLowPoints(heightMap)
	risk := integers.Sum(lowPoints...) + len(lowPoints)
	return risk
}

func Part2(input []string) (count int) {
	return
}

func makeHeightmap(input []string) (heights [][]int) {
	for _, line := range input {
		if values := []int{}; line != "" {
			for _, v := range line {
				point := string(v)
				values = append(values, parse.ToInt(point))
			}
			heights = append(heights, values)
		}
	}
	return heights
}

func findLowPoints(heights [][]int) (lowPoints []int) {
	var directions = func(x, y int) (directions [][]int) {
		if x != 0 {
			directions = append(directions, []int{-1, 0})
		}
		if x != len(heights[0])-1 {
			directions = append(directions, []int{1, 0})
		}
		if y != 0 {
			directions = append(directions, []int{0, -1})
		}
		if y != len(heights)-1 {
			directions = append(directions, []int{0, 1})
		}
		return directions
	}

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
				lowPoints = append(lowPoints, heights[y][x])
			}
		}
	}
	return lowPoints
}
