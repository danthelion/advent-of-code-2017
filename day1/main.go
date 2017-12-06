package main

import (
	"io/ioutil"
	"fmt"
	"strconv"
)

func check(e error) {
	if e != nil {
		panic(e)
	}
}

func main() {
	b, err := ioutil.ReadFile("input")
	check(err)

	// Convert input to str
	str := string(b)

	// Half of Captcha Length
	cap_len := int(len(str) / 2)

	sum := 0

	// Iterate over string
	for i, e := range str {

		// Convert pos and char to ints
		element, err := strconv.ParseInt(string(e), 10, 64)
		check(err)

		index := int(i)
		fmt.Printf("character %d starts at byte position %d\n", element, index)

		nxt := index + cap_len

		if nxt >= len(str) {
			n, err := strconv.ParseInt(string(str[index-cap_len]), 10, 64)
			check(err)
			if int(element) == int(n) {
				sum += int(element)
			}
		} else {
			n, err := strconv.ParseInt(string(str[nxt]), 10, 64)
			check(err)
			if int(element) == int(n) {
				sum += int(element)
			}
		}
	}

	println(sum)
}
