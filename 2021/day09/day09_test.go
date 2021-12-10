package main

import "testing"

var input = []string{
	"2199943210",
	"3987894921",
	"9856789892",
	"8767896789",
	"9899965678",
}

func TestPart1(t *testing.T) {
	result := Part1(input)
	reference := 15
	if result != reference {
		t.Errorf("Result was incorrect, got: %d, want: %d.", result, reference)
	}
}

func TestPart2(t *testing.T) {
	result := Part2(input)
	reference := 1134
	if result != reference {
		t.Errorf("Result was incorrect, got: %d, want: %d.", result, reference)
	}
}
