package integers

import "testing"

func TestOddMedian(t *testing.T) {
	type args struct {
		vals []int
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		{name: "already sorted", args: args{vals: []int{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}}, want: 6},
		{name: "normal case", args: args{vals: []int{5, 3, 28, 12, 35, 9, 0, 8, 6, 1, 2}}, want: 6},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := OddMedian(tt.args.vals...); got != tt.want {
				t.Errorf("OddMedian() = %v, want %v", got, tt.want)
			}
		})
	}
}
