package collections

// Stack is a LIFO data structure.
type Stack struct {
	items []interface{}
}

// Push adds a new item to the stack.
func (s *Stack) Push(item interface{}) {
	s.items = append(s.items, item)
}

// Pop removes and returns the last item of the stack.
func (s *Stack) Pop() interface{} {
	if s.Empty() {
		return nil
	}
	item := s.items[s.Len()-1]
	s.items = s.items[:s.Len()-1]
	return item
}

// Peek returns the last item of the stack without removing it.
func (s *Stack) Peek() interface{} {
	if s.Empty() {
		return nil
	}
	return s.items[s.Len()-1]
}

// Len returns the length of the stack.
func (s *Stack) Len() int {
	return len(s.items)
}

// Empty returns true if the stack is empty.
func (s *Stack) Empty() bool {
	return !s.NotEmpty()
}

// Not empty returns true if the stack is not empty.
func (s *Stack) NotEmpty() bool {
	return s.Len() > 0
}
