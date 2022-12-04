package main

import (
	"fmt"
	"strings"

	"github.com/dratzinger/Advent-of-Code/2022/util/parse"
)

func main() {
	in := parse.StrLines("input.txt")
	fmt.Println("Day X - Pt. 1:", Part1(in))
	fmt.Println("Day X - Pt. 2:", Part2(in))
}

type assignment struct {
	from, to int
}

type assignmentPair struct {
	a, b assignment
}

func Part1(input []string) (count int) {
	assignments := parseAssignments(input)
	for _, pair := range assignments {
		if fullyCovered(pair.a, pair.b) {
			count++
		}
	}
	return count
}

func fullyCovered(a, b assignment) bool {
	return a.from <= b.from && a.to >= b.to || b.from <= a.from && b.to >= a.to
}

func parseAssignments(input []string) (pairs []assignmentPair) {
	for _, line := range input {
		if line != "" {
			pair := parsePair(line)
			pairs = append(pairs, pair)
		}
	}
	return pairs
}

func parsePair(line string) assignmentPair {
	raw := strings.Split(line, ",")
	temp := strings.Split(raw[0], "-")
	a := parse.IntSlice(temp)
	temp = strings.Split(raw[1], "-")
	b := parse.IntSlice(temp)

	return assignmentPair{
		a: assignment{
			from: a[0],
			to:   a[1],
		},
		b: assignment{
			from: b[0],
			to:   b[1],
		},
	}
}

func Part2(input []string) (count int) {
	assignments := parseAssignments(input)
	for _, pair := range assignments {
		if overlaps(pair.a, pair.b) {
			count++
		}
	}
	return count
}

func overlaps(a, b assignment) bool {
	for i := a.from; i <= a.to; i++ {
		if i >= b.from && i <= b.to {
			return true
		}
	}
	return false
}
