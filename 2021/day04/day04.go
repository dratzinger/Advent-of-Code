package main

import (
	"fmt"
	"strings"

	parse "github.com/dratzinger/Advent-of-Code/2021/util"
	"gonum.org/v1/gonum/mat"
)

func main() {
	content := parse.Read("input.txt")
	in := parse.Blocks(content, "\n\n")
	fmt.Println("Day 2 - Pt. 1:", Part1(in))
	fmt.Println("Day 2 - Pt. 2:", Part2(in))
}

func Part1(input []string) (score int) {
	nums := strings.Split(input[0], ",")
	draws := parse.IntSlice(nums)
	boards := makeBoards(input[1:])
	checked := makeChecked(len(boards))

	for _, call := range draws {
		winner := playBingo(call, &boards, &checked)
		if winner != -1 {
			score = mat.Mul(boards[winner], checked[winner])
		}
	}
	return
}

func Part2(input []string) (count int) {
	return
}

func makeBoards(data []string) (boards []mat.Matrix) {
	for _, board := range data {
		boards = append(boards, parse.Matrix(board, 5, 5))
	}
	return boards
}

func makeChecked(count int) (checked []mat.Matrix) {
	for i := 0; i < count; i++ {
		var zeros [25]float64
		checked = append(checked, mat.NewDense(5, 5, zeros[:]))
	}
	return checked
}

func playBingo(call int, boards, checked *[]mat.Matrix) int {
	return 0
}

func sum(unchecked mat.Matrix) int {
	return 0
}
