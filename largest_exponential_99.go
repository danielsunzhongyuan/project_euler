package main

import (
	"fmt"
	"io/ioutil"
	"math"
	"sort"
	"strconv"
	"strings"
)

type ExpNumber struct {
	Base     int
	Exponent int
	Data     float64
}

type ExpNumbers []ExpNumber

func (e ExpNumbers) Len() int {
	return len(e)
}

func (e ExpNumbers) Swap(i, j int) {
	e[i], e[j] = e[j], e[i]
}

func (e ExpNumbers) Less(i, j int) bool {
	return e[i].Data < e[j].Data
}

func main() {
	f, err := ioutil.ReadFile("p099_base_exp.txt")
	if err != nil {
		fmt.Println("Can't open file", err)
		return
	}
	x := string(f)
	lines := strings.Split(x, "\n")
	numbers := make(ExpNumbers, 1000)
	for i, line := range lines {
		tmp := strings.Split(line, ",")
		b, _ := strconv.Atoi(tmp[0])
		e, _ := strconv.Atoi(tmp[1])
		numbers[i] = ExpNumber{Base: b, Exponent: e, Data: float64(e) * math.Log2(float64(b))}
	}
	sort.Sort(numbers)
	fmt.Println(numbers[999])
}
