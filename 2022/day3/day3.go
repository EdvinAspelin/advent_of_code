package main

import (
	"fmt"
	"bufio"
	"os"
	"strings"
)

type Rucksack struct {
	compartments []string
}

type Group struct {
	rucksacks []string
}

func main() {
	printPrioritySum()
	printGroupPrioritySum()
}

func printGroupPrioritySum() {
	groups := parseGroups()

	priority_sum := 0
	for _, group := range groups {
		badge := getBadge(group.rucksacks)
		priority_sum += getPriority(badge)
	}

	fmt.Print("Solution part 2: ")
	fmt.Print(priority_sum)
	fmt.Print("\n")
}

func printPrioritySum() {
	rucksacks := parseRucksacks()

	priority_sum := 0
	for _, rucksack := range rucksacks {
		duplicate := getDuplicate(rucksack.compartments)

		priority_sum += getPriority(duplicate)
	}

	fmt.Print("Solution part 1: ")
	fmt.Print(priority_sum)
	fmt.Print("\n")
}

func getPriority(rune_value rune) int {
	value := int(rune_value)

	if value < 97 {
		return value - 38
	} else {
		return value - 96
	}
}

func getDuplicate(compartments []string) rune {
	for _, item := range compartments[0] {
		if strings.ContainsRune(compartments[1], item) {
			return item
		}
	}

	return 0
}

func getBadge(rucksacks []string) rune {
	for _, badge := range rucksacks[0] {
		if strings.ContainsRune(rucksacks[1], badge) &&
			strings.ContainsRune(rucksacks[2], badge) {
			return badge
		}
	}

	return 0
}

func parseRucksacks() []Rucksack {
	readFile, err := os.Open("input.txt")

	if err != nil {
		fmt.Print("Can't load file")
	}

	fileScanner := bufio.NewScanner(readFile)

	rucksacks := []Rucksack{}
	for fileScanner.Scan() {
		content := fileScanner.Text()

		rucksack := parseRucksack(content)

		rucksacks = append(rucksacks, rucksack)
	}

	return rucksacks
}

func parseGroups() []Group {
	readFile, err := os.Open("input.txt")

	if err != nil {
		fmt.Print("Can't load file")
	}

	fileScanner := bufio.NewScanner(readFile)

	groups := []Group{}
	for {
		group := Group{}
		
		for ii := 0; ii < 3; ii++ {
			if fileScanner.Scan() {
				group.rucksacks = append(group.rucksacks, fileScanner.Text())
			} else {
				return groups
			}
		}

		groups = append(groups, group)
	}
}

func parseRucksack(content string) Rucksack {
	rucksack := Rucksack{}

	rucksack.compartments = append(rucksack.compartments, content[0:len(content) / 2])
	rucksack.compartments = append(rucksack.compartments, content[len(content) / 2:len(content)])

	return rucksack
}