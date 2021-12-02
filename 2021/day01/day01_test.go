package main

import "testing"

var input = []int{199, 200, 208, 210, 200, 207, 240, 269, 260, 263}

func TestPart1(t *testing.T) {
	result := Part1(input)
	reference := 7
	if result != reference {
		t.Errorf("Result was incorrect, got: %d, want: %d.", result, reference)
	}
}

func TestPart2(t *testing.T) {
	result := Part2(input)
	reference := 5
	if result != reference {
		t.Errorf("Result was incorrect, got: %d, want: %d.", result, reference)
	}
}
