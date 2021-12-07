package integers

import "sort"

func Abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}

func AbsDiff(a, b int) int {
	return Abs(a - b)
}

func Extrema(vals ...int) (min, max int) {
	min = vals[0]
	max = vals[0]
	for _, v := range vals {
		if v > max {
			max = v
		} else if v < min {
			min = v
		}
	}
	return min, max
}

func Even(x int) bool {
	return x%2 == 0
}

func Odd(x int) bool {
	return !Even(x)
}

func Max(vals ...int) int {
	_, max := Extrema(vals...)
	return max
}

func Min(vals ...int) int {
	min, _ := Extrema(vals...)
	return min
}

func Range(vals ...int) int {
	min, max := Extrema(vals...)
	return max - min
}

func Sum(vals ...int) (sum int) {
	for _, val := range vals {
		sum += val
	}
	return sum
}

func Mean(vals ...int) float64 {
	sum := Sum(vals...)
	n := len(vals)
	return float64(sum) / float64(n)
}

func Median(vals ...int) float64 {
	sorted := sort.IntSlice(vals)
	length := len(vals)
	middle := length / 2

	if Odd(length) {
		return float64(sorted[middle])
	}
	return Mean(sorted[middle-1] + sorted[middle])
}
