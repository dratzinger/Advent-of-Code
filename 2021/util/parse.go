package parse

import (
	"log"
	"os"
	"strconv"
	"strings"
)

func Read(filename string) string {
	data, err := os.ReadFile(filename)
	if err != nil {
		log.Fatal(err)
	}
	return string(data)
}

func StrLines(filename string) []string {
	content := Read(filename)
	return strings.Split(content, "\n")
}

func IntLines(filename string) (ints []int) {
	lines := StrLines(filename)
	return IntSlice(lines)
}

func IntSlice(input []string) (ints []int) {
	for _, line := range input {
		if line != "" {
			ints = append(ints, ToInt(line))
		}
	}
	return ints
}

func ToInt(str string) int {
	val, err := strconv.Atoi(str)

	if err != nil {
		log.Fatal(err)
	}
	return val
}

func IntBlocks(input []string, colSep string, blockSep string) (blocks [][][]int) {
	block := [][]int{}
	for i, line := range input {
		if line == blockSep || i == len(input)-1 {
			blocks = append(blocks, block)
			block = [][]int{}
		} else {
			row := strings.Split(line, colSep)
			conv := IntSlice(row)
			block = append(block, conv)
		}
	}
	return blocks
}
