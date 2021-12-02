package parse

import (
	"fmt"
	"io"
	"os"
)

func IntLines(filename string) []int {
	file, err := os.Open(filename)

	if err != nil {
		fmt.Println(err)
		os.Exit(1)
	}

	var line int
	var nums []int

	for {
		// give a pattern to scan
		_, err := fmt.Fscanf(file, "%d\n", &line)

		if err != nil {
			if err == io.EOF {
				// stop reading the file
				break
			}
			fmt.Println(err)
			os.Exit(1)
		}
		nums = append(nums, line)
	}
	return nums
}
