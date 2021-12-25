package main

import "testing"

var input = []string{
	"5483143223",
	"2745854711",
	"5264556173",
	"6141336146",
	"6357385478",
	"4167524645",
	"2176841721",
	"6882881134",
	"4846848554",
	"5283751526",
}

func TestPart1(t *testing.T) {
	result := Part1(input)
	reference := 1656
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
