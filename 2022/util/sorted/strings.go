package sorted

import "sort"

// sort characters in a string in alphabetical order
func String(input string) string {
	runes := []rune(input)
	sort.Slice(runes, func(i, j int) bool {
		return runes[i] < runes[j]
	})
	return string(runes)
}

// sort characters in a slice of strings in alphabetical order
func StringSlice(in []string) (out []string) {
	for _, s := range in {
		out = append(out, String(s))
	}
	return
}

// sort integers in a slice in descending order
func IntSliceDesc(input []int) []int {
	ints := []int(input)
	sort.Slice(ints, func(i, j int) bool {
		return ints[i] > ints[j]
	})
	return ints
}
