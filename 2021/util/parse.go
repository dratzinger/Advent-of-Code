package parse

import (
	"bufio"
	"log"
	"os"
	"strconv"
)

func StrLines(filename string) (parsed []string) {
	file, err := os.Open(filename)
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)

	for scanner.Scan() {
		parsed = append(parsed, scanner.Text())
	}

	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}
	return parsed
}

func IntLines(filename string) (ints []int) {
	return IntSlice(StrLines(filename))
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
