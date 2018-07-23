package main

import (
	"fmt"
	"sync"
)

var (
	MaxNumber = 50000000
	wg        sync.WaitGroup
)

func main() {
	results := make(map[int]bool)
	wg.Add(1)
	primes := make(chan int)
	p := make([]int, 0)
	go printPrime(primes)
	for prime := range primes {
		p = append(p, prime)
	}
	wg.Wait()
	//fmt.Println(len(p), p)

	for _, base4 := range p {
		tmp := pow(base4, 4)
		if tmp > MaxNumber {
			break
		}
		for _, base3 := range p {
			tmp1 := tmp + pow(base3, 3)
			if tmp1 > MaxNumber {
				break
			}
			for _, base2 := range p {
				tmp2 := tmp1 + pow(base2, 2)
				if tmp2 > MaxNumber {
					break
				}
				//fmt.Println(base2, "* 2 +", base3, "* 3 +", base4, "* 4 =", tmp2)
				results[tmp2] = true
			}
		}
	}
	fmt.Println(len(results))
}

func printPrime(primes chan<- int) {
next:
	for outer := 2; outer < 7100; outer++ {
		for inner := 2; inner < outer; inner++ {
			if outer%inner == 0 {
				continue next
			}
		}
		primes <- outer
	}
	wg.Done()
	close(primes)
}

func pow(x, y int) int {
	res := 1
	for i := 0; i < y; i++ {
		res *= x
	}
	return res
}
