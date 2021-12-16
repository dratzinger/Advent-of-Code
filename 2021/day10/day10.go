package main

import (
	"fmt"

	"github.com/dratzinger/Advent-of-Code/2021/util/collections"
	"github.com/dratzinger/Advent-of-Code/2021/util/integers"
	"github.com/dratzinger/Advent-of-Code/2021/util/parse"
)

var errorPoints = map[rune]int{
	')': 3,
	']': 57,
	'}': 1197,
	'>': 25137,
}

var completionPoints = map[rune]int{
	')': 1,
	']': 2,
	'}': 3,
	'>': 4,
}

var closing = map[rune]rune{
	'(': ')',
	'[': ']',
	'<': '>',
	'{': '}',
}

func main() {
	in := parse.StrLines("input.txt")
	fmt.Println("Day 10 - Pt. 1:", Part1(in))
	fmt.Println("Day 10 - Pt. 2:", Part2(in))
}

var corrupted map[int]rune
var completionScores []int

func Part1(input []string) (sum int) {
	corrupted, completionScores = errorCheck(input)
	for _, bracket := range corrupted {
		sum += errorPoints[bracket]
	}
	return sum
}

func Part2(input []string) (median int) {
	if completionScores == nil {
		Part1(input)
	}
	return integers.OddMedian(completionScores...)
}

func errorCheck(input []string) (corrupted map[int]rune, scores []int) {
	corrupted = make(map[int]rune)

	for i, line := range input {
		open := new(collections.Stack)

		// Check for errors
		lineValid := func() bool {
			for _, bracket := range line {
				switch bracket {
				case '(', '[', '{', '<':
					open.Push(bracket)
				case ')', ']', '}', '>':
					lastOpened := open.Pop().(rune)
					if closing[lastOpened] != bracket {
						corrupted[i] = bracket
						return false
					}
				}
			}
			return true
		}

		// Check for completion
		completionScore := func() (score int) {
			for open.NotEmpty() {
				closable := open.Pop().(rune)
				closer := closing[closable]
				score *= 5
				score += completionPoints[closer]
			}
			return score
		}

		notCorrupted := lineValid()
		score := completionScore()
		if notCorrupted && score > 0 {
			scores = append(scores, score)
		}
	}
	return corrupted, scores
}
