package main

import (
	"fmt"

	"github.com/dratzinger/Advent-of-Code/2021/util/collections"
	"github.com/dratzinger/Advent-of-Code/2021/util/parse"
)

var points = map[rune]int{
	')': 3,
	']': 57,
	'}': 1197,
	'>': 25137,
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

func Part1(input []string) (sum int) {
	corrupted = findCorrupted(input)
	for _, bracket := range corrupted {
		sum += points[bracket]
	}
	return sum
}

func Part2(input []string) (count int) {
	if corrupted == nil {
		corrupted = findCorrupted(input)
	}
	return
}

func findCorrupted(input []string) map[int]rune {
	corrupted := make(map[int]rune)

	for i, line := range input {
		open := new(collections.Stack)
	lineCheck:
		for _, bracket := range line {
			switch bracket {
			case '(', '[', '{', '<':
				open.Push(bracket)
			case ')', ']', '}', '>':
				lastOpened := open.Pop()
				if lastOpened == nil || closing[lastOpened.(rune)] != bracket {
					corrupted[i] = bracket
					break lineCheck
				}
			}
		}
	}
	return corrupted
}
