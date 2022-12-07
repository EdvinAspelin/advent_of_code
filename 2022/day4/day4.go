package main

import (
	"fmt"
	"bufio"
	"os"
	"strings"
	"strconv"
)

func main() {
	readFile, err := os.Open("input.txt")

	if err != nil {
		fmt.Print("Can't load file")
	}

	fileScanner := bufio.NewScanner(readFile)

	counter := 0
	for fileScanner.Scan() {
		orders := strings.Split(fileScanner.Text(), ",")
		
		order0 := parseInterval(orders[0])
		order1 := parseInterval(orders[1])

		if isFullyContained(order0, order1) || isFullyContained(order1, order0) {
			counter += 1
		}
	}

	print("Solution part 1: ")
	print(counter)
	print("\n")
}

func isFullyContained(interval0 []int, interval1 []int) bool {
	if interval1[0] >= interval0[0] && interval1[0] <= interval0[1] {
		if interval1[1] <= interval0[1] {
			return true
		}
	}

	return false
}

func parseInterval(interval string) []int {
	interval_int := []int{}

	for _, value := range strings.Split(interval, "-") {
		value_int, _ := strconv.Atoi(value)
		interval_int = append(interval_int, value_int)
	}

	return interval_int
}
