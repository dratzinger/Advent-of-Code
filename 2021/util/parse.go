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
