package parse

import (
	"bytes"
	"log"
	"os"
	"strconv"
	"strings"

	"gonum.org/v1/gonum/mat"
)

func Read(filename string) string {
	data, err := os.ReadFile(filename)
	if err != nil {
		log.Fatal(err)
	}
	norm := normalizeNewlines(data)
	return string(norm)
}

func StrLines(filename string) []string {
	content := Read(filename)
	return strings.Split(content, "\n")
}

func Int(input string, base int) int64 {
	val, err := strconv.ParseInt(input, 2, 64)

	if err != nil {
		log.Fatal(err)
	}
	return val
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

func FloatSlice(input []string) (nums []float64) {
	for _, line := range input {
		if line != "" {
			nums = append(nums, ToFloat(line))
		}
	}
	return nums
}

func ToFloat(str string) float64 {
	val, err := strconv.ParseFloat(str, 64)

	if err != nil {
		log.Fatal(err)
	}
	return val
}

func Blocks(content string, delim string) []string {
	return strings.Split(content, delim)
}

func Matrix(content string, rows, cols int) mat.Matrix {
	sep := " "
	stripped := strings.Replace(content, "\n", sep, -1)
	data := strings.Split(stripped, sep)
	values := FloatSlice(data)
	return mat.NewDense(rows, cols, values)
}

func IntBlock(input, colSep, rowSep string) (block [][]int) {
	if input != "" {
		for _, line := range strings.Split(input, rowSep) {
			if line != "" {
				row := strings.Split(line, colSep)
				conv := IntSlice(row)
				block = append(block, conv)
			}
		}
	}
	return block
}

// From Essential Go:
// NormalizeNewlines normalizes \r\n (windows) and \r (mac)
// into \n (unix)
func normalizeNewlines(d []byte) []byte {
	// replace CR LF \r\n (windows) with LF \n (unix)
	d = bytes.Replace(d, []byte{13, 10}, []byte{10}, -1)
	// replace CF \r (mac) with LF \n (unix)
	d = bytes.Replace(d, []byte{13}, []byte{10}, -1)
	return d
}
