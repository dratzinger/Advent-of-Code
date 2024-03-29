package main

import "testing"

var input = []string{}

func TestPart1(t *testing.T) {
	result := Part1(input)
	reference := -1
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
