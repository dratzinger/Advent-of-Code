package integers

func Abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}

func Max(vals ...int) int {
	max := vals[0]
	for _, v := range vals {
		if v > max {
			max = v
		}
	}
	return max
}

func Min(vals ...int) int {
	min := vals[0]
	for _, v := range vals {
		if v < min {
			min = v
		}
	}
	return min
}

func Sum(vals ...int) (sum int) {
	for _, val := range vals {
		sum += val
	}
	return sum
}
