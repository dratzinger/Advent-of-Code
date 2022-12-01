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
