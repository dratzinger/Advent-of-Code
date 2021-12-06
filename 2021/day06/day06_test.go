package main

import (
	"strings"
	"testing"
)

const example = "3,4,3,1,2"

var input = strings.Split(example, ",")

func TestPart1(t *testing.T) {
	result := Part1(input)
	reference := 5934
	if result != reference {
		t.Errorf("Result was incorrect, got: %d, want: %d.", result, reference)
	}
}

func TestPart2(t *testing.T) {
	result := Part2(input)
	reference := 26984457539
	if result != reference {
		t.Errorf("Result was incorrect, got: %d, want: %d.", result, reference)
	}
}
