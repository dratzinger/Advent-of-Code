package main

import "github.com/dratzinger/Advent-of-Code/2022/util/parse"

// A simple tree data structure
type Filetree struct {
	Root    *Dir
	Current *Dir
}
type Dir struct {
	Parent *Dir
	Name   string
	Files  []*File
	Dirs   map[string]*Dir
}
type File struct {
	Name string
	Size int
}

func (t *Filetree) AddDir(name string) {
	dir := &Dir{
		Name:   name,
		Parent: t.Current,
		Dirs:   make(map[string]*Dir),
		Files:  make([]*File, 0),
	}

	if t.Root == nil {
		t.Root = dir
	}

	if t.Current != nil {
		t.Current.Dirs[name] = dir
	} else {
		t.Current = dir
	}
}

func (t *Filetree) AddFile(name, size string) {
	file := File{Name: name, Size: parse.ToInt(size)}
	t.Current.Files = append(t.Current.Files, &file)
}

func (t *Filetree) ChangeDir(name string) {
	if name == "/" {
		t.Current = t.Root
	} else if name == ".." {
		if t.Current.Parent != nil {
			t.Current = t.Current.Parent
		}
	} else {
		t.Current = t.Current.Dirs[name]
	}
}

// recursively add file sizes
func (dir *Dir) sumSizes() (total int) {
	for _, file := range dir.Files {
		total += file.Size
	}
	for _, d := range dir.Dirs {
		total += d.sumSizes()
	}
	return
}

// recursively walk the tree and sum dir sizes up to a certain threshold
// (files are summed multiple times)
func (t *Filetree) SumDirs(threshold int) (total int) {
	return t.Root.sumDirs(threshold)
}

func (dir *Dir) sumDirs(threshold int) (total int) {
	if dir.sumSizes() <= threshold {
		total += dir.sumSizes()
	}
	for _, d := range dir.Dirs {
		total += d.sumDirs(threshold)
	}
	return
}
