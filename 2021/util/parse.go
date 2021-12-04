package parse

import (
	"log"
	"os"
	"strconv"
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
		val, err := strconv.Atoi(line)

		if err != nil {
			log.Fatal(err)
		}
		ints = append(ints, val)
	}
	return ints
}
