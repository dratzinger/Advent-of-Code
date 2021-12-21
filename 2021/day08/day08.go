package main

import (
	"fmt"
	"strings"

	"github.com/dratzinger/Advent-of-Code/2021/util/parse"
	"github.com/dratzinger/Advent-of-Code/2021/util/sorted"
)

func main() {
	in := parse.Stripped("input.txt")
	fmt.Println("Day 8 - Pt. 1:", Part1(in))
	fmt.Println("Day 8 - Pt. 2:", Part2(in))
}

var unique = map[int]int{
	2: 1,
	3: 7,
	4: 4,
	7: 8,
}

func Part1(input []string) (count int) {
	for _, line := range input {
		_, signal := prepareLine(line)
		for _, segments := range signal {
			_, found := unique[len(segments)]
			if found {
				count++
			}
		}
	}
	return
}

func Part2(input []string) (count int) {
	for _, line := range input {
		patterns, value := prepareLine(line)
		resolved := resolvePatterns(patterns)
		count += mapValue(resolved, value)
	}
	return
}

func prepareLine(input string) (patterns, value []string) {
	blocks := strings.Split(input, " | ")
	patterns = strings.Split(blocks[0], " ")
	patterns = sorted.StringSlice(patterns)
	value = strings.Split(blocks[1], " ")
	value = sorted.StringSlice(value)
	return
}

func resolvePatterns(patterns []string) map[string]byte {
	resolved := make(map[string]byte)
	known := make(map[int]string)

	fiveLen := []string{} // strings of length 5
	sixLen := []string{}  // strings of length 6

	for _, pattern := range patterns {
		switch len(pattern) {
		case 2, 3, 4, 7:
			number := unique[len(pattern)]
			known[number] = pattern
			resolved[pattern] = byte(number)
		case 5:
			fiveLen = append(fiveLen, pattern)
		case 6:
			sixLen = append(sixLen, pattern)
		}
	}

	for k, v := range resolveFiveLen(fiveLen, known) {
		resolved[k] = v
	}

	for k, v := range resolveSixLen(sixLen, known) {
		resolved[k] = v
	}
	return resolved
}

func resolveFiveLen(candidates []string, known map[int]string) map[string]byte {
	resolved := make(map[string]byte)
	for _, pattern := range candidates {
		if findDifference(pattern, known[7]) == 3 {
			resolved[pattern] = byte(2)
		}

		if findDifference(pattern, known[1]) == 4 {
			resolved[pattern] = byte(5)
		}
	}
	remaining := candidates[0]
	resolved[remaining] = byte(3)
	return resolved
}

func resolveSixLen(candidates []string, known map[int]string) map[string]byte {
	panic("unimplemented")
}

// find the number of characters that are contained in
// one string but not the other
func findDifference(s1, s2 string) (count int) {
	for _, c := range s1 {
		if !strings.Contains(s2, string(c)) {
			count++
		}
	}
	return
}

func mapValue(resolved map[string]byte, value []string) int {
	valueBytes := []byte{}
	for _, v := range value {
		if val, found := resolved[v]; !found {
			panic("pattern not found")
		} else {
			valueBytes = append(valueBytes, val)
		}
	}
	result := string(valueBytes)
	return parse.ToInt(result)
}
