package main

import "testing"

var input = []string{
	"2-4,6-8",
	"2-3,4-5",
	"5-7,7-9",
	"2-8,3-7",
	"6-6,4-6",
	"2-6,4-8",
}

func TestPart1(t *testing.T) {
	result := Part1(input)
	reference := 2
	if result != reference {
		t.Errorf("Result was incorrect, got: %d, want: %d.", result, reference)
	}
}

func TestPart2(t *testing.T) {
	result := Part2(input)
	reference := -1
	if result != reference {
		t.Errorf("Result was incorrect, got: %d, want: %d.", result, reference)
	}
}
