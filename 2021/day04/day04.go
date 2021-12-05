package main

import (
	"fmt"
	"strings"

	"github.com/dratzinger/Advent-of-Code/2021/util/integers"
	"github.com/dratzinger/Advent-of-Code/2021/util/parse"
)

func main() {
	content := parse.Read("input.txt")
	in := parse.Blocks(content, "\n\n")
	fmt.Println("Day 4 - Pt. 1:", Part1(in))
	fmt.Println("Day 4 - Pt. 2:", Part2(in))
}

type board struct {
	data           [][]int
	rowMin, colMin int // -5 in any row or column wins
}

func Part1(input []string) int {
	nums := strings.Split(input[0], ",")
	draws := parse.IntSlice(nums)
	boards := makeBoards(input[1:])

	for _, call := range draws {
		winners := playBingo(call, boards)
		if len(winners) > 0 {
			return call * score(&boards[winners[0]])
		}
	}
	return -1
}

func Part2(input []string) (count int) {
	nums := strings.Split(input[0], ",")
	draws := parse.IntSlice(nums)
	boards := makeBoards(input[1:])

	for _, call := range draws {
		winners := playBingo(call, boards)
		if len(winners) > 0 {
			if len(boards) == 1 {
				return call * score(&boards[0])
			}
			for i, winner := range winners {
				boards = removeBoard(boards, winner-i)
			}
		}
	}
	return -1
}

func makeBoards(data []string) (boards []board) {
	for _, val := range data {
		nums := parse.IntBlock(val, " ", "\n")
		board := board{data: nums}
		boards = append(boards, board)
	}
	return boards
}

func playBingo(call int, boards []board) (winners []int) {
	for i, b := range boards {
		markCalled(call, &b)
		won := b.colMin < -4 || b.rowMin < -4
		if won {
			winners = append(winners, i)
		}
	}
	return winners
}

// mark call with -1 and recalculate stats
func markCalled(called int, board *board) {
	for y, row := range board.data {
		for x, val := range row {
			if val == called {
				board.data[y][x] = -1
				updateMins(board, y, x)
			}
		}
	}
}

func updateMins(board *board, row, col int) {
	board.colMin = integers.Min(sumCol(board.data, col), board.colMin)
	board.rowMin = integers.Min(sumRow(board.data, row), board.rowMin)
}

func sumRow(data [][]int, row int) (sum int) {
	for _, val := range data[row] {
		sum += val
	}
	return sum
}

func sumCol(data [][]int, col int) (sum int) {
	for _, row := range data {
		sum += row[col]
	}
	return sum
}

func score(board *board) (sum int) {
	for _, row := range board.data {
		for _, val := range row {
			if val > -1 {
				sum += val
			}
		}
	}
	return sum
}

func removeBoard(boards []board, i int) []board {
	boards[i] = boards[len(boards)-1]
	return boards[:len(boards)-1]
}
