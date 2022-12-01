package collections

import "github.com/dratzinger/Advent-of-Code/2022/util/parse"

type IntMatrix [][]int
type Point struct {
	x, y int
}
type Direction Point

func Parse(input []string) IntMatrix {
	return parse.IntMatrix(input)
}

func (mat *IntMatrix) Rows() int {
	return len(*mat)
}

func (mat *IntMatrix) Cols() int {
	if mat.Rows() < 1 {
		return 0
	}
	return len((*mat)[0])
}

func (mat *IntMatrix) Directions(x, y, neighbours int) (directions []Direction) {
	if !(neighbours == 4 || neighbours == 8) {
		panic("invalid neighbourhood")
	}
	if neighbours >= 4 {
		if x != 0 {
			directions = append(directions, Direction{-1, 0})
		}
		if x != mat.Cols()-1 {
			directions = append(directions, Direction{1, 0})
		}
		if y != 0 {
			directions = append(directions, Direction{0, -1})
		}
		if y != mat.Rows()-1 {
			directions = append(directions, Direction{0, 1})
		}
	}
	if neighbours == 8 {

	}
	return directions
}
