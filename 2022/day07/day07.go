package main

import (
	"fmt"
	"strings"

	"github.com/dratzinger/Advent-of-Code/2022/util/collections"
	"github.com/dratzinger/Advent-of-Code/2022/util/parse"
)

func main() {
	in := parse.StrLines("input.txt")
	fmt.Println("Day 7 - Pt. 1:", Part1(in))
	fmt.Println("Day 7 - Pt. 2:", Part2(in))
}

func Part1(input []string) (total int) {
	fileTree := buildTree(input)
	return fileTree.SumDirs(100000)
}

func buildTree(input []string) *Filetree {
	tree := Filetree{}
	tree.AddDir("/")
	terminal := collections.Stack{}

	for i := len(input) - 1; i >= 0; i-- {
		if input[i] != "" {
			feed := strings.Split(input[i], " ")
			terminal.Push(feed)
		}
	}

	for terminal.NotEmpty() {
		line := terminal.Pop().([]string)
		if line[0] == "$" {
			switch line[1] {
			case "cd":
				tree.ChangeDir(line[2])
			case "ls":
				for terminal.NotEmpty() && terminal.Peek().([]string)[0] != "$" {
					item := terminal.Pop().([]string)
					if item[0] == "dir" {
						tree.AddDir(item[1])
					} else {
						tree.AddFile(item[1], item[0])
					}
				}
			}
		}
	}
	return &tree
}

func Part2(input []string) (total int) {
	return
}
