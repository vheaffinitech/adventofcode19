package main

import (
	"fmt"
	"io/ioutil"
	"strconv"
	"strings"
)

func main() {
	dat, err := ioutil.ReadFile("input.txt")
	check(err)
	//fmt.Print(string(dat))
	lines := strings.Split(string(dat), "\n")
	total := 0
	for _, x := range lines {
		total = total + CalculateFuel(x)
	}

	fmt.Println(total)
	//fmt.Println(CalculateFuel("1969"))

}

func check(e error) {
	if e != nil {
		panic(e)
	}
}

func CalculateFuel(s string) int {
	fmt.Println(s)
	i, err := strconv.Atoi(s)
	check(err)
	result := 0
	if i > 1 {
		r := int(i/3) - 2
		if r < 0 {
			r = 0
		}
		result = r + CalculateFuel(strconv.Itoa(r))
	}
	return result
}
