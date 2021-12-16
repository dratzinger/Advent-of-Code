package main

import (
	"fmt"
	"sort"

	"github.com/dratzinger/Advent-of-Code/2021/util/collections"
	"github.com/dratzinger/Advent-of-Code/2021/util/integers"
	"github.com/dratzinger/Advent-of-Code/2021/util/parse"
)

type point struct {
	x, y int
}
type direction point

func main() {
	in := parse.StrLines("input.txt")
	fmt.Println("Day 9 - Pt. 1:", Part1(in))
	fmt.Println("Day 9 - Pt. 2:", Part2(in))
}

func Part1(input []string) (risk int) {
	heightMap, lowPoints := prepare(input)
	for _, p := range lowPoints {
		risk += 1 + heightMap[p.y][p.x]
	}
	return risk
}

func Part2(input []string) (count int) {
	heightMap, lowPoints := prepare(input)
	basinLimit := 9

	basins := []int{}
	data := makeMapData(heightMap)
	for _, v := range lowPoints {
		size := data.floodBasin(point{v.x, v.y}, basinLimit)
		basins = append(basins, size)
	}
	// sort the basins
	sort.IntSlice(basins).Sort()
	topThree := basins[len(basins)-3:]

	return integers.Product(topThree...)
}

func prepare(input []string) (heightMap [][]int, lowPoints []point) {
	heightMap = makeHeightmap(input)
	lowPoints = findLowPoints(heightMap)
	return heightMap, lowPoints
}

var directions func(int, int) []direction

func makeHeightmap(input []string) (heights [][]int) {
	heights = parse.IntMatrix(input)
	directions = makeDirectionFn(len(heights[0])-1, len(heights)-1)
	return heights
}

func makeDirectionFn(maxX, maxY int) func(int, int) []direction {
	var dirFn = func(x, y int) (directions []direction) {
		if x != 0 {
			directions = append(directions, direction{-1, 0})
		}
		if x != maxX {
			directions = append(directions, direction{1, 0})
		}
		if y != 0 {
			directions = append(directions, direction{0, -1})
		}
		if y != maxY {
			directions = append(directions, direction{0, 1})
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
					if heights[y+direction.y][x+direction.x] <= height {
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

type mapData struct {
	values  [][]int
	visited [][]bool
}

func makeMapData(vals [][]int) mapData {
	rowLen := len(vals[0])
	visited := make([][]bool, len(vals))
	for i := range vals {
		visited[i] = make([]bool, rowLen)
	}
	return mapData{
		values:  vals,
		visited: visited,
	}
}

func (m *mapData) floodBasin(seed point, threshold int) (size int) {
	s := new(collections.Stack)
	s.Push(seed)
	for s.NotEmpty() {
		p := s.Pop().(point)
		x, y := p.x, p.y
		if !m.visited[y][x] && m.values[y][x] < threshold {
			size++
			m.visited[y][x] = true
			for _, direction := range directions(x, y) {
				s.Push(point{x + direction.x, y + direction.y})
			}
		}
	}
	return size
}
