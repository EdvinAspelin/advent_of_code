package main

import (
	"bufio"
	"fmt"
	"os"
	"log"
	"strings"
	"strconv"
)

var input_path = "input.txt"

func main() {
	input, error := os.Open(input_path)

	if error != nil {
		log.Fatal(error)
	}

	scanner := bufio.NewScanner(input)

	my_points := 0
	for scanner.Scan() {
		match := strings.Split(scanner.Text(), " ")

		opponent_sign := value(match[0])
		my_sign := predictSign(opponent_sign, match[1])

		match_result := battle(my_sign, opponent_sign)

		my_points += match_result + my_sign
	}

	fmt.Printf("My result: %s", strconv.Itoa(my_points))
}

func predictSign(opponent_sign int, outcome string) int {
	if outcome == "X" {
		return ((opponent_sign + 1) % 3) + 1
	}
	if outcome == "Y" {
		return opponent_sign
	}
	if outcome == "Z" {
		return (opponent_sign % 3) + 1
	}

	fmt.Printf("Invalid outcome input")
	return 0
}

func battle(my_value int, opponent_value int) int {
	result := my_value - opponent_value

	if result == 0 {
		return 3
	}
	if (result == 1) || (result == -2) {
		return 6
	}

	return 0
}

func value(sign string) int {
	if (sign == "A") || (sign == "X") {
		return 1
	}
	if (sign == "B") || (sign == "Y") {
		return 2
	}
	if (sign == "C") || (sign == "Z") {
		return 3
	}

	return 0
}